"""Text extraction and exact quote matching (stdlib + the pdftotext binary).

Quote matching is *exact after normalisation* — never fuzzy. Normalisation
only removes differences that are artefacts of extraction, not of wording:

* Unicode compatibility forms, curly quotes → straight, dashes → '-', NBSP and
  other spaces → ' ', soft hyphens removed;
* page/star markers removed: [*12], {**40 NY3d at 407}, [PDF page 3];
* a hyphen at a line end followed by a lower-case letter is tried three ways —
  joined and dropped ("postcon-\\nviction" → "postconviction"), joined and
  kept ("specific-\\nvictim" → "specific-victim"), and left as is;
* all whitespace runs → one space.

Anything else — a changed word, a dropped "not", different punctuation
inside the quote — is a mismatch. A case-only difference is reported as such.
"""
import html
import html.parser
import re
import shutil
import subprocess
import tempfile
import unicodedata

MARKER_RX = re.compile(r"\[\*+\d+\]|\{\*\*[^}]{1,60}\}|\[PDF page \d+\]")
_TRANS = str.maketrans({
    "‘": "'", "’": "'", "‚": "'", "‛": "'", "′": "'",
    "“": '"', "”": '"', "„": '"', "″": '"',
    "‐": "-", "‑": "-", "‒": "-", "–": "-", "—": "-",
    "―": "-", "−": "-", " ": " ", " ": " ", " ": " ",
    "­": None, "﻿": None,
})


# ------------------------------------------------------------------ extraction
def pdf_pages(pdf_bytes, layout=True):
    """Return a list of page texts (pdftotext, -layout by default; layout=False
    gives pdftotext's raw reading order, which is right where -layout scrambles
    hanging-indent lists)."""
    if not shutil.which("pdftotext"):
        raise RuntimeError("pdftotext is not installed (poppler-utils)")
    with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
        f.write(pdf_bytes)
        f.flush()
        args = ["pdftotext"] + (["-layout"] if layout else []) + ["-enc", "UTF-8", f.name, "-"]
        out = subprocess.run(args,
                             capture_output=True, check=True).stdout
    pages = out.decode("utf-8", "replace").split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    return pages


class _HTMLText(html.parser.HTMLParser):
    BLOCK = {"p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6",
             "section", "article", "blockquote", "pre", "table", "dd", "dt", "hr"}
    SKIP = {"script", "style", "noscript", "template", "svg", "head"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        elif tag in self.BLOCK:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self.skip:
            self.skip -= 1
        elif tag in self.BLOCK:
            self.out.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def _sniff_encoding(b, declared=None):
    """Header charset > <meta charset> > BOM > strict UTF-8 > Windows-1252."""
    if declared:
        return declared
    if b[:3] == b"\xef\xbb\xbf":
        return "utf-8-sig"
    m = re.search(rb"""<meta[^>]+charset\s*=\s*["']?([\w-]+)""", b[:4096], re.I)
    if m:
        return m.group(1).decode("ascii", "replace")
    try:
        b.decode("utf-8")
        return "utf-8"
    except UnicodeDecodeError:
        return "cp1252"


class _Links(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.links, self._href, self._text = [], None, []

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self._href = dict(attrs).get("href")
            self._text = []

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self._href is not None:
            self.links.append((self._href, re.sub(r"\s+", " ", "".join(self._text)).strip()))
            self._href = None


def html_links(html_bytes, base_url, encoding=None):
    """Return [(absolute_url, link_text)] for every <a href> on the page."""
    import urllib.parse
    enc = _sniff_encoding(html_bytes, encoding)
    try:
        s = html_bytes.decode(enc, "replace")
    except LookupError:
        s = html_bytes.decode("utf-8", "replace")
    p = _Links()
    p.feed(s)
    out = []
    for href, text in p.links:
        if not href or href.startswith(("javascript:", "mailto:", "#")):
            continue
        out.append((urllib.parse.urljoin(base_url, html.unescape(href)), text))
    return out


def html_text(html_bytes, encoding=None):
    enc = _sniff_encoding(html_bytes, encoding)
    if enc.lower() in ("iso-8859-1", "latin-1", "latin1", "us-ascii", "ascii"):
        enc = "cp1252"          # what browsers actually use for these labels
    try:
        s = html_bytes.decode(enc, "replace")
    except LookupError:
        s = html_bytes.decode("utf-8", "replace")
    p = _HTMLText()
    p.feed(s)
    text = html.unescape("".join(p.out))
    text = re.sub(r"[ \t]+\n", "\n", text)
    return re.sub(r"\n{3,}", "\n\n", text).strip()


# ------------------------------------------------------------------ matching
MODES = ("drop", "keep", "none")   # line-end hyphen: join & drop it / join & keep it / leave as is


def _mode(join_hyphens):
    if join_hyphens is True:
        return "drop"
    if join_hyphens is False or join_hyphens is None:
        return "none"
    return join_hyphens


def _norm_with_map(text, join_hyphens="drop"):
    """Normalise text; return (normalised, offsets) mapping each char back.

    join_hyphens: "drop"  'postcon-\\nviction' -> 'postconviction'
                  "keep"  'specific-\\nvictim' -> 'specific-victim'
                  "none"  leave line breaks as spaces ('specific- victim')
    """
    mode = _mode(join_hyphens)
    text = MARKER_RX.sub(lambda m: " " * len(m.group(0)), text)
    out, offs = [], []
    i, n = 0, len(text)
    while i < n:
        ch = unicodedata.normalize("NFKC", text[i]).translate(_TRANS)
        if mode != "none" and ch == "-" and i + 1 < n and text[i + 1] in "\r\n":
            j = i + 1
            while j < n and text[j] in " \t\r\n":
                j += 1
            if j < n and text[j].islower():
                if mode == "keep":
                    out.append("-")
                    offs.append(i)
                i = j
                continue
        for c in ch:
            if c.isspace():
                if out and out[-1] == " ":
                    continue
                c = " "
            out.append(c)
            offs.append(i)
        i += 1
    return "".join(out), offs


def normalise(text, join_hyphens="drop"):
    return _norm_with_map(text, join_hyphens)[0].strip()


def find_quote(text, quote):
    """Search text for quote under each hyphenation mode.

    Returns dict(found, case_only, start, end, mode)."""
    q = normalise(quote, "none")
    if not q:
        return {"found": False, "case_only": False}
    hays = [(m,) + _norm_with_map(text, m) for m in MODES]
    for m, hay, offs in hays:
        k = hay.find(q)
        if k >= 0:
            return {"found": True, "case_only": False, "start": offs[k],
                    "end": offs[k + len(q) - 1] + 1, "mode": f"line-end hyphens: {m}"}
    for m, hay, offs in hays:
        k = hay.lower().find(q.lower())
        if k >= 0:
            return {"found": False, "case_only": True, "start": offs[k],
                    "end": offs[k + len(q) - 1] + 1, "mode": "case-differs"}
    return {"found": False, "case_only": False}


def longest_prefix_found(text, quote):
    """Diagnostics for a miss: how many leading words of the quote do match."""
    words = normalise(quote, "none").split(" ")
    hays = [normalise(text, m) for m in MODES]
    lo, hi = 0, len(words)
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if any(" ".join(words[:mid]) in h for h in hays):
            lo = mid
        else:
            hi = mid - 1
    return lo, len(words)

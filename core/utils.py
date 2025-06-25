import html
import re

_TAG_RE = re.compile(r"<[^>]+>")


def sanitize_html(text: str) -> str:
    """Remove HTML tags and escape remaining content."""
    without_tags = _TAG_RE.sub("", text)
    return html.escape(without_tags)

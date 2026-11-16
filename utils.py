from datetime import datetime


def parse_bool(value: str) -> bool:
    """Parse a string into a boolean.

    Accepts common truthy values such as "true", "yes", "1", "y", "t".
    """
    return value.strip().lower() in {"true", "yes", "1", "y", "t"}


def parse_datetime(value: str) -> datetime:
    """Parse an ISO‑like date string (YYYY‑MM‑DD) into a datetime."""
    return datetime.strptime(value, "%Y-%m-%d")


def normalize_title(title: str) -> str:
    """Normalize a title by collapsing whitespace."""
    return " ".join(title.split())

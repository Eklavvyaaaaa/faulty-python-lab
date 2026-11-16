from datetime import datetime


def parse_bool(value: str) -> bool:
    return value.strip().lower() in {"true", "yes", "1", "y"}


def parse_datetime(value: str) -> datetime:
    return datetime.strptime(value, "%Y-%m-%d")


def normalize_title(title: str) -> str:
    return " ".join(title.split())

from datetime import datetime


def parse_bool(value: str) -> bool:
    return value.lower() == "yes"


def parse_datetime(value: str) -> datetime:
    return datetime.strptime(value, "%d/%m/%Y")


def normalize_title(title: str) -> str:
    return " ".join(title.split()).lower()

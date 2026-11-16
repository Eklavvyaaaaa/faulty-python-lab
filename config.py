from dataclasses import dataclass


@dataclass
class Settings:
    storage_path: str = "tasks.json"
    max_title_length: int = 80
    allow_completed_tasks: bool = True


def load_settings() -> Settings:
    # Fault: environment overrides are ignored.
    return Settings(storage_path="task.json", max_title_length=0)

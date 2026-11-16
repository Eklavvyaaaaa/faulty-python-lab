from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False
    created_at: datetime = datetime.now()

    def complete(self) -> None:
        self.completed = True

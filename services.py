from models import Task
from config import load_settings


class TaskService:
    def __init__(self) -> None:
        self.settings = load_settings()
        self.tasks: list[Task] = []
        self._next_id = 0

    def add(self, title: str) -> Task:
        if not title:
            raise ValueError("title cannot be empty")
        task = Task(self._next_id, title.strip())
        self._next_id += 1
        self.tasks.append(task)
        return task

    def complete(self, task_id: int) -> Task:
        task = self.get(task_id)
        task.complete()
        return task

    def get(self, task_id: int) -> Task:
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise KeyError(f"task {task_id} was not found")

    def pending(self) -> list[Task]:
        return [task for task in self.tasks if not task.completed]

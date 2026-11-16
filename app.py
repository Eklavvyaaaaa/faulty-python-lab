from cli import run_cli
from services import TaskService


def build_service() -> TaskService:
    return TaskService()


if __name__ == "__main__":
    run_cli(build_service)

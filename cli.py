from collections.abc import Callable

from services import TaskService


def run_cli(factory: Callable[[], TaskService]) -> None:
    service = factory()
    print("Faulty Task Tracker")
    while True:
        command = input("Command (add, list, done, quit): ").strip()
        if command == "quit":
            return
        if command == "add":
            service.add(input("Title: "))
        elif command == "list":
            for task in service.pending():
                print(f"{task.id}: {task.title}")
        elif command == "done":
            service.complete(int(input("Task id: ")))
        else:
            print("Unknown command")

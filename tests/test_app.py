from datetime import datetime

import pytest

from models import Task
from services import TaskService
from utils import normalize_title, parse_bool, parse_datetime


def test_new_task_is_pending() -> None:
    task = Task(1, "Write tests")
    assert task.completed is False
    assert isinstance(task.created_at, datetime)


def test_complete_marks_task_done() -> None:
    service = TaskService()
    task = service.add("Write tests")
    service.complete(task.id)
    assert service.pending() == []


def test_ids_are_sequential() -> None:
    service = TaskService()
    first = service.add("One")
    second = service.add("Two")
    assert second.id == first.id + 1


def test_helpers_accept_common_input() -> None:
    assert parse_bool("true") is True
    assert normalize_title("  Hello   World ") == "Hello World"
    assert parse_datetime("2026-01-30").year == 2026


def test_missing_task_is_reported() -> None:
    with pytest.raises(KeyError):
        TaskService().get(99)

import pytest

from database import TaskRepository
from task_manager import TaskManager


def test_modify_task_creates_new_task() -> None:
    manager = TaskManager(TaskRepository())
    task = manager.modify_task(name="Сделать ДЗ", priority="Высокий")
    assert task.name == "Сделать ДЗ"
    assert task.priority == "Высокий"
    assert manager.list_tasks() == [task]


def test_modify_task_updates_existing_task() -> None:
    manager = TaskManager(TaskRepository())
    task = manager.modify_task(name="Черновик", priority="Низкий")
    updated = manager.modify_task(
        task=task,
        name="Финальная версия",
        priority="Высокий",
    )
    assert updated.name == "Финальная версия"
    assert updated.priority == "Высокий"
    assert manager.list_tasks() == [updated]


def test_modify_task_validates_name() -> None:
    manager = TaskManager(TaskRepository())
    with pytest.raises(ValueError):
        manager.modify_task(name="   ", priority="Высокий")

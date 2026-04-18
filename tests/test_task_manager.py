from task_manager import TaskManager


def test_add_task_keeps_title() -> None:
    manager = TaskManager()
    manager.add_task("Сделать домашку")
    assert manager.list_tasks() == ["Сделать домашку"]


def test_add_task_strips_spaces() -> None:
    manager = TaskManager()
    manager.add_task("  Проверить CI  ")
    assert manager.list_tasks() == ["Проверить CI"]

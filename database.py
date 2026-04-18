"""Storage layer for TaskManager entities."""

from models import Task


class TaskRepository:
    """In-memory repository for tasks."""

    def __init__(self) -> None:
        self._tasks: list[Task] = []

    def save(self, task: Task) -> None:
        self._tasks.append(task)

    def update(self, old_task: Task, new_task: Task) -> None:
        for index, existing_task in enumerate(self._tasks):
            if existing_task == old_task:
                self._tasks[index] = new_task
                return
        raise ValueError("Task does not exist")

    def list_all(self) -> list[Task]:
        return list(self._tasks)

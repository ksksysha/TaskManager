"""Simple task manager module for CI checks."""


class TaskManager:
    """Stores and retrieves task titles."""

    def __init__(self) -> None:
        self._tasks: list[str] = []

    def add_task(self, title: str) -> None:
        normalized_title = title.strip()
        if not normalized_title:
            raise ValueError("Task title must not be empty")
        self._tasks.append(normalized_title)

    def list_tasks(self) -> list[str]:
        return list(self._tasks)

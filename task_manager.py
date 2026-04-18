"""Task management logic for the TaskManager project."""

from database import TaskRepository
from models import Task


class TaskManager:
    """Provides high-level operations for creating and updating tasks."""

    def __init__(self, repository: TaskRepository) -> None:
        self._repository = repository

    def modify_task(
        self,
        task: Task | None = None,
        name: str = "",
        priority: str = "",
    ) -> Task:
        """Create a new task or update an existing one."""
        normalized_name = name.strip()
        normalized_priority = priority.strip()
        if not normalized_name:
            raise ValueError("Task name must not be empty")
        if not normalized_priority:
            raise ValueError("Task priority must not be empty")

        if task is None:
            new_task = Task(name=normalized_name, priority=normalized_priority)
            self._repository.save(new_task)
            return new_task

        updated_task = Task(name=normalized_name, priority=normalized_priority)
        self._repository.update(task, updated_task)
        return updated_task

    def list_tasks(self) -> list[Task]:
        """Return all tasks from storage."""
        return self._repository.list_all()

"""Domain models used by TaskManager."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Task:
    """Represents a task entity."""

    name: str
    priority: str

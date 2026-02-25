from dataclasses import dataclass
from enum import Enum


class TaskStatus(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


@dataclass
class Task:
    id: int
    description: str
    status: TaskStatus
    createdAt: str
    updatedAt: str | None = None
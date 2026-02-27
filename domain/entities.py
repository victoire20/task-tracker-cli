from dataclasses import dataclass
from enum import Enum


class AppConfig:
    NAME = "task-cli"
    VERSION = "1.0.0"
    LIST_COMMANDS = ['add', 'update', 'delete', 'mark-in-progress', 'mark-done', 'list']
    LIST_STATUS = ['todo', 'in-progress', 'done']


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
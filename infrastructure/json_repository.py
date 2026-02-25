import json
from pathlib import Path

from domain.entities import Task


class JsonTaskRepository:
    def __init__(self, file_path: str | None = ''):
        self.file_path = Path(file_path)

    def load(self) -> list[Task]:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        if not self.file_path.exists():
            self.file_path.write_text("[]")
            return []

        with self.file_path.open('r') as f:
            data = json.load(f)

        return [Task(**item) for item in data]

    def save(self, tasks: list[Task]) -> None:
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with self.file_path.open('w') as f:
            json.dump([task.__dict__ for task in tasks], f, indent=4)
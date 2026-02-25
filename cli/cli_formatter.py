from domain.entities import Task
from utils.date_formatter import format_datetime


class TaskCLIFormatter:

    def render(self, tasks: list[Task]) -> str:
        widths = {
            "id": 3,
            "description": 20,
            "status": 12,
            "createdAt": 20,
            "updatedAt": 20
        }

        lines = []

        header = (
            f"{'id':<{widths['id']}} "
            f"{'description':<{widths['description']}} "
            f"{'status':<{widths['status']}} "
            f"{'createdAt':<{widths['createdAt']}} "
            f"{'updatedAt':<{widths['updatedAt']}}"
        )

        separator = (
            f"{'-' * widths['id']} "
            f"{'-' * widths['description']} "
            f"{'-' * widths['status']} "
            f"{'-' * widths['createdAt']} "
            f"{'-' * widths['updatedAt']}"
        )

        lines.append(header)
        lines.append(separator)

        if not tasks:
            lines.append("No tasks found")
            return "\n".join(lines)

        for task in tasks:
            lines.append(
                f"{task.id:<{widths['id']}} "
                f"{task.description:<{widths['description']}} "
                f"{task.status:<{widths['status']}} "
                f"{format_datetime(task.createdAt):<{widths['createdAt']}} "
                f"{format_datetime(task.updatedAt):<{widths['updatedAt']}}"
            )

        return "\n".join(lines)
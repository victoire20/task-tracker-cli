import textwrap

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


class TaskClIHelperFormatter:
    def render(self) -> str:
        lines = textwrap.dedent("""
            task-cli - simple task tracker from the command line

            USAGE:
              task-cli [command] [flags]

            DESCRIPTION:
              A CLI tool to manage your tasks locally.
              Tasks are stored in a JSON file on your machine.

            COMMANDS:
              add        Add a new task
              update     Update an existing task
              delete     Delete a task
              mark-in-progress       Mark a task as in-progress
              mark-done       Mark a task as done
              list       List tasks (todo, in-progress, done)

            FLAGS:
              -h, --help     Show help for task-cli
              -v, --version  Show version information

            EXAMPLES:
              task-cli add "Buy groceries"
              task-cli update 1 "Buy groceries and cook dinner"
              task-cli delete 1
              task-cli mark 1 in-progress
              task-cli mark 1 done
              task-cli list
              task-cli list done

            Use "task-cli [command] --help" for more information about a command.
        """).strip()

        return lines
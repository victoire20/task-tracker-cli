from application.task_service import TaskService
from domain.entities import TaskStatus

from cli.commands_impl import add_commands, update_commands, delete_commands, change_status_commands, list_commands

LIST_COMMANDS = ['add', 'update', 'delete', 'mark-in-progress', 'mark-done', 'list']
LIST_STATUS = ['todo', 'in-progress', 'done']


def handle_command(cmd: list[str], service: TaskService):
    if len(cmd) < 2:
        print(f"You must use one of these commands: {', '.join(LIST_COMMANDS)}")
        return

    command = cmd[1].lower()

    if command not in LIST_COMMANDS:
        print(f"{command} is not a valid task-cli command")
        return

    # ---------- Add ----------
    if command == 'add':
        if len(cmd) != 3:
            print("Usage: task-cli add <task_title>")
            return
        add_commands(cmd[2], service)
        return

    # ---------- Update ----------
    if command == 'update':
        if len(cmd) != 4:
            print("Usage: task-cli update <task_id> <new_title>")
            return
        try:
            task_id = int(cmd[2])
        except ValueError:
            print("Task ID must be an integer")
            return
        update_commands(task_id, cmd[3], service)
        return

    # ---------- Delete ----------
    if command == 'delete':
        if len(cmd) != 3:
            print("Usage: task-cli delete <task_id>")
            return
        try:
            task_id = int(cmd[2])
        except ValueError:
            print("Task ID must be an integer")
            return
        delete_commands(task_id, service)
        return

    # ---------- Change status ----------
    if command == 'mark-in-progress':
        if len(cmd) != 3:
            print("Usage: task-cli mark-in-progress <task_id>")
            return
        try:
            task_id = int(cmd[2])
        except ValueError:
            print("Task ID must be an integer")
            return
        change_status_commands(task_id, TaskStatus.IN_PROGRESS, service)
        return

    if command == 'mark-done':
        if len(cmd) != 3:
            print("Usage: task-cli mark-done <task_id>")
            return
        try:
            task_id = int(cmd[2])
        except ValueError:
            print("Task ID must be an integer")
            return
        change_status_commands(task_id, TaskStatus.DONE, service)
        return

    # ---------- List ----------
    if command == 'list':
        if len(cmd) == 2:
            # Liste complète
            list_commands(service)
            return
        elif len(cmd) == 3:
            # Liste filtrée par status
            status_str = cmd[2].lower()
            if status_str not in LIST_STATUS:
                print(f"Invalid status. Must be one of: {', '.join(LIST_STATUS)}")
                return
            # Conversion string -> TaskStatus
            status_enum = TaskStatus(status_str)
            list_commands(service, status_enum)
            return
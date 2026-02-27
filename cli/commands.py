from application.task_service import TaskService
from cli.cli_formatter import TaskClIHelperFormatter
from domain.entities import TaskStatus, AppConfig

from cli.commands_impl import add_commands, update_commands, delete_commands, change_status_commands, list_commands


def handle_command(cmd: list[str], service: TaskService):
    if not cmd or cmd[0] != "task-cli":
        raise ValueError("Invalid command")

    if len(cmd) == 1:
        output = TaskClIHelperFormatter()
        print(output.render(), end='\n\n')
        return

    if len(cmd) == 2 and cmd[1].lower() in ['-h', '--help']:
        output = TaskClIHelperFormatter()
        print(output.render(), end='\n\n')
        return

    if len(cmd) == 2 and cmd[1].lower() in ['-v', '--version']:
        print(f"{AppConfig.NAME} version {AppConfig.VERSION}")
        return

    command = cmd[1].lower()

    if command not in AppConfig.LIST_COMMANDS:
        print(f"{command} is not a valid task-cli command")
        return

    # ---------- Add ----------
    if command == 'add':
        if len(cmd) != 3:
            print("Usage: task-cli add <task_title>")
            return
        add_commands(cmd[2], service)
        list_commands(service)
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
        list_commands(service)
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
        list_commands(service)
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
        list_commands(service)
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
        list_commands(service)
        return

    # ---------- List ----------
    if command == 'list':
        if len(cmd) == 2:
            # Complete list
            list_commands(service)
            return
        elif len(cmd) == 3:
            # List filtered by status
            status_str = cmd[2].lower()
            if status_str not in AppConfig.LIST_STATUS:
                print(f"Invalid status. Must be one of: {', '.join(AppConfig.LIST_STATUS)}")
                return
            # Conversion string -> TaskStatus
            status_enum = TaskStatus(status_str)
            list_commands(service, status_enum)
            return

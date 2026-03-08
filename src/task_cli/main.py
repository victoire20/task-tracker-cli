#!/usr/bin/env python3
import argparse

from task_cli.application.task_service import TaskService
from task_cli.cli.commands_impl import list_commands, add_commands, update_commands, change_status_commands, \
    delete_commands
from task_cli.domain.entities import TaskStatus
from task_cli.infrastructure.json_repository import JsonTaskRepository

def create_parser():
    parser = argparse.ArgumentParser(
        prog="task-cli",
        usage="task-cli [command] [flags]",
        description="A CLI tool to manage your tasks locally. Tasks are stored in a JSON file on your machine.",
        epilog="Use \"task-cli [command] --help\" for more information about a command",
        exit_on_error=False
    )

    parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.0")

    subparsers = parser.add_subparsers(title="commands", dest="command")

    # exit
    exit_parser = subparsers.add_parser("exit", aliases=["quit", "exit()", "quit()"], help='exit the program')

    # add
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("description", help="Task description")

    # list
    list_parser = subparsers.add_parser("list", help="List tasks (todo, in-progress, done)")
    list_parser.add_argument(
        "-s", "--status",
        choices=["todo", "in-progress", "done"],
        help="Filter tasks by status",
        required=False
    )

    # update
    update_parser = subparsers.add_parser("update", help="Update an existing task")
    update_parser.add_argument("id", type=int, help="Task ID")
    update_parser.add_argument("description", help="Task description")

    # delete
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("id", type=int, help="Task ID")

    # in progress
    in_progress_parser = subparsers.add_parser("mark-in-progress", help='Mark a task as in-progress')
    in_progress_parser.add_argument("id", type=int, help="Task ID")

    # done
    done_parser = subparsers.add_parser("mark-done", help="Mark a task as done")
    done_parser.add_argument("id", type=int, help="Task ID")

    return parser


def main():
    parser = create_parser()
    try:
        args = parser.parse_args()

        repository = JsonTaskRepository("src/task_cli/data/tasks.json")
        service = TaskService(repository)

        print("Task Tracker CLI started. Type 'exit', 'exit()', 'quit', or 'quit()' to quit.")
        print("This tool helps you manage your projects efficiently.")
        print("Use 'task-cli --help' to see available commands.", end="\n\n")

        if not args.command:
            parser.print_help()

        if args.command == 'add':
            add_commands(args.description, service)

        if args.command == "list":
            if args.status is None:
                list_commands(service)
            else:
                list_commands(service, args.status)

        if args.command == "update":
            update_commands(args.id, args.description, service)
            list_commands(service)

        if args.command == "mark-in-progress":
            change_status_commands(args.id, TaskStatus.IN_PROGRESS, service)
            list_commands(service)

        if args.command == "mark-done":
            change_status_commands(args.id, TaskStatus.DONE, service)
            list_commands(service)

        if args.command == 'delete':
            delete_commands(args.id, service)
            list_commands(service)
    except argparse.ArgumentError as e:
        print(f"Error ArgumentError : {e}")
    except SystemExit as e:
        exc_type = e.__class__.__name__
        print(f"[Error argparse] Type: {exc_type}, code: {e.code}")
    except Exception as e:
        print(f"[Error unknow] {type(e).__name__}: {e}")
        return None


if __name__ == "__main__":
    main()

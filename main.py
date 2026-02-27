import shlex
from infrastructure.json_repository import JsonTaskRepository
from application.task_service import TaskService
from cli.commands import handle_command

if __name__ == "__main__":
    repository = JsonTaskRepository("./data/tasks.json")
    service = TaskService(repository)

    print("Task Tracker CLI started. Type 'exit', 'exit()', 'quit', or 'quit()' to quit.")

    try:
        while True:
            user_input = input(">> ").strip()
            if not user_input:
                continue

            cmd = shlex.split(user_input)

            if cmd[0].lower() in ["exit", "exit()", "quit", "quit()"]:
                print("Exiting...")
                break

            if cmd[0].lower() != "task-cli":
                print(f"{cmd[0]} is not a task-cli command")
                continue

            handle_command(cmd, service)

    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)
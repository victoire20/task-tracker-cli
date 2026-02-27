from application.task_service import TaskService
from cli.cli_formatter import TaskCLIFormatter
from domain.entities import TaskStatus


def add_commands(description, service: TaskService):
    task_id = service.add_task(description)
    print(f"Task added successfully (ID: {task_id})", end="\n\n")

def list_commands(service: TaskService, status: TaskStatus | None = None):
    tasks_list = service.list_tasks()
    if status:
        tasks_list = [task for task in tasks_list if task.status == status]
    output = TaskCLIFormatter()
    print(output.render(tasks_list), end="\n\n")

def change_status_commands(task_id: int, status: TaskStatus, service: TaskService):
    service.change_task_status(task_id, status)

def update_commands(task_id: int, description: str, service):
    service.update_task(task_id, description)

def delete_commands(task_id: int, service):
    service.delete_task(task_id)
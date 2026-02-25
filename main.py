import os
from dataclasses import dataclass
from datetime import datetime
import shlex
import json
from enum import Enum

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


JSON_FILE = os.path.join("./data/", 'tasks.json')

def read_data():
    try:
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        with open(JSON_FILE, 'w') as f:
            json.dump([], f)
        return []
    except FileNotFoundError:
        with open(JSON_FILE, 'x') as f:
            pass
        return []


def add_item(item: Task):
    try:
        data = read_data()
        data.append(item.__dict__)
        with open(JSON_FILE, 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except PermissionError as e:
        print(f"PermissionError: {e}")


def create_task(description: str) -> Task:
    data = read_data()
    return Task(id=len(data) + 1, description=description, status=TaskStatus.TODO, createdAt=str(datetime.now()))


def get_task_by_id(task_id: int) -> int | None:
    if not task_id:
        return None
    data = read_data()
    return next((i for i, t in enumerate(data) if t["id"] == task_id), None)


def update_task_by_id(task_id: int, description: str):
    task_index = get_task_by_id(task_id)
    data = read_data()
    if task_index and task_index >= 0:
        data[task_index]['description'] = description
        data[task_index]['updatedAt'] = str(datetime.now())
        try:
            with open(JSON_FILE, 'w', encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except PermissionError as e:
            print(f"PermissionError: {e}")


def delete_task_by_id(task_id: int):
    task_index = get_task_by_id(task_id)
    data = read_data()
    if task_index is not None and task_index >= 0:
        del data[task_index]
        try:
            with open(JSON_FILE, 'w', encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except PermissionError as e:
            print(f"PermissionError: {e}")

def change_status(task_id: int, status: TaskStatus):
    task_index = get_task_by_id(task_id)
    data = read_data()
    if task_index is not None and task_index >= 0:
        data[task_index]['status'] = status.value
        data[task_index]['updatedAt'] = str(datetime.now())
        try:
            with open(JSON_FILE, 'w', encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
        except PermissionError as e:
            print(f"PermissionError: {e}")

def get_all_tasks(status: TaskStatus | None = None) -> list[Task]:
    data = read_data()
    if status:
        return list(filter(lambda t: t["status"] == status, data))
    return data


def format_datetime(dt_str: str | None = None) -> str:
    if  not dt_str:
        return '-'
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S.%f")
    return dt.strftime("%d/%m/%Y %H:%M")


if __name__ == '__main__':
    try:
        while True:
            cmd = shlex.split(input())
            if cmd[0].lower() == 'exit':
                exit(0)

            if len(cmd) < 2:
                print(f"You must use one of these commands to run the program:  {', '.join(LIST_COMMANDS)}")
                continue

            if cmd[0].lower() != 'task-cli':
                print(f"{cmd[0]} is not a task-cli command")
                continue

            if cmd[1].lower() not in LIST_COMMANDS:
                print(f"{cmd[0]}: {cmd[1]} is not a task-cli command")
                continue

            if cmd[1].lower() == LIST_COMMANDS[0] and len(cmd) == 3:
                task = create_task(description=cmd[2])
                add_item(task)
                print(f"Task added successfully (ID: {task.id})")
                continue

            if cmd[1].lower() == LIST_COMMANDS[1] and len(cmd) == 4:
                update_task_by_id(int(cmd[2]), cmd[3])
                continue

            if cmd[1].lower() == LIST_COMMANDS[2] and len(cmd) == 3:
                delete_task_by_id(int(cmd[2]))
                continue

            if cmd[1].lower() == LIST_COMMANDS[3] and len(cmd) == 3:
                change_status(int(cmd[2]), TaskStatus.IN_PROGRESS)
                continue

            if cmd[1].lower() == LIST_COMMANDS[4] and len(cmd) == 3:
                change_status(int(cmd[2]), TaskStatus.DONE)
                continue

            if cmd[1].lower() == LIST_COMMANDS[5] and len(cmd) == 2:
                all_tasks = get_all_tasks()
                print()
                print(f"{'id':<3} {'description':<20} {'status':<12} {'createdAt':<20} {'updatedAt':<20}")
                print(f"{'-' * 3} {'-' * 20} {'-' * 12} {'-' * 20} {'-' * 20}")
                for task in all_tasks:
                    print(
                        str(task['id']).ljust(3),
                        task['description'].ljust(20),
                        task['status'].ljust(12),
                        str(format_datetime(task['createdAt'])).ljust(20),
                        str(format_datetime(task['updatedAt'])).ljust(20)
                    )
                print()
                continue

            if cmd[1].lower() == LIST_COMMANDS[5] and len(cmd) == 2:
                pass
    except ValueError as e:
        print(f"ValueError: {e}")
    except KeyboardInterrupt:
        exit(0)
    except AttributeError as e:
        print(f"AttributeError: {e}")


from datetime import datetime
from domain.entities import Task, TaskStatus
from utils.date_formatter import format_datetime


class TaskService:
    def __init__(self, repository):
        self.repository = repository

    def add_task(self, description: str) -> int:
        tasks = self.repository.load()
        new_task = Task(
            id=len(tasks) + 1,
            description=description,
            status=TaskStatus.TODO,
            createdAt=str(datetime.now())
        )
        tasks.append(new_task)
        self.repository.save(tasks)

        return new_task.id

    def get_task_index(self, task_id: int) -> int:
        tasks = self.list_tasks()
        return next((i for i, t in enumerate(tasks) if t.id == task_id), -1)

    def list_tasks(self, task_status: TaskStatus | None = None) -> list[Task]:
        tasks = self.repository.load()

        if task_status is not None:
            tasks = [task for task in tasks if task.status == task_status]

        return sorted(tasks, key=lambda t: t.id)

    def update_task(self, task_id: int,  description: str):
        tasks = self.repository.load()
        task_index = self.get_task_index(task_id)

        if task_index != -1:
            tasks[task_index].description = description
            tasks[task_index].updatedAt = str(datetime.now())
            self.repository.save(tasks)

    def change_task_status(self, task_id: int, status: TaskStatus):
        tasks = self.repository.load()
        task_index = self.get_task_index(task_id)

        if task_index != -1:
            tasks[task_index].status = status
            tasks[task_index].updatedAt = str(datetime.now())
            self.repository.save(tasks)

    def delete_task(self, task_id: int):
        tasks = self.repository.load()
        task_index = self.get_task_index(task_id)

        if task_index != -1:
            del tasks[task_index]
            self.repository.save(tasks)



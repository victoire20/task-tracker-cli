import unittest
from datetime import datetime

from cli.cli_formatter import TaskCLIFormatter
from domain.entities import Task, TaskStatus


class TestTaskCLIFormatter(unittest.TestCase):
    def test_task_formatter_render_with_empty_data(self):
        formatter = TaskCLIFormatter()
        tasks = []
        output = formatter.render(tasks)

        self.assertIn('No tasks found', output)

    def test_task_formatter_render_with_tasks(self):
        formatter = TaskCLIFormatter()
        tasks = [
            Task(id=1, description="Task 1", status=TaskStatus.TODO, createdAt=str(datetime.now()))
        ]
        output = formatter.render(tasks)

        self.assertIn('Task 1', output)
        self.assertIn('id', output)


if __name__ == '__main__':
    unittest.main()

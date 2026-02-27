import textwrap
import unittest
from datetime import datetime

from cli.cli_formatter import TaskCLIFormatter, TaskClIHelperFormatter
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

class TestTaskClIHelperFormatter(unittest.TestCase):
    def test_task_formatter_render(self):
        formatter = TaskClIHelperFormatter()
        output = formatter.render()

        self.assertIn('add        Add a new task', output)
        self.assertIn('update     Update an existing task', output)
        self.assertIn('delete     Delete a task', output)
        self.assertIn('mark-in-progress       Mark a task as in-progress', output)
        self.assertIn('mark-done       Mark a task as done', output)
        self.assertIn('list       List tasks (todo, in-progress, done)', output)
        self.assertIn('FLAGS:', output)
        self.assertIn('-h, --help     Show help for task-cli', output)
        self.assertIn('-v, --version  Show version information', output)


if __name__ == '__main__':
    unittest.main()

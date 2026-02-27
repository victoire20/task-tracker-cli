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
        output_expected = textwrap.dedent("""
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
              
        """).strip()
        output = formatter.render()

        self.assertEqual(output, output_expected)


if __name__ == '__main__':
    unittest.main()

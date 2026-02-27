import io
import os
import textwrap
import unittest
from unittest.mock import patch

from application.task_service import TaskService
from cli.commands import handle_command
from domain.entities import AppConfig, Task, TaskStatus
from infrastructure.json_repository import JsonTaskRepository


class TestHandleCommand(unittest.TestCase):
    def setUp(self):
        self.file_path = '../data/test_tasks.json'
        self.repo = JsonTaskRepository(self.file_path)
        self.service = TaskService(self.repo)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    @unittest.skip("Test temporairement désactivé")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_helper_documentation(self, mock_stdout):
        cmd = ['task-cli']
        handle_command(cmd, self.service)
        expected_output = textwrap.dedent("""
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

        self.assertEqual(mock_stdout.getvalue(), f"{expected_output}\n\n")

        cmd = ['task-cli', '-h']
        handle_command(cmd, self.service)
        expected_output = textwrap.dedent("""
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

        #self.assertEqual(mock_stdout.getvalue(), f"{expected_output}\n\n")

        cmd = ['task-cli', '--help']
        handle_command(cmd, self.service)
        expected_output = textwrap.dedent("""
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

        #self.assertEqual(mock_stdout.getvalue(), f"{expected_output}\n\n")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_version(self, mock_stdout):
        cmd = ['task-cli', '-v']
        handle_command(cmd, self.service)
        expected_output = f'{AppConfig.NAME} version {AppConfig.VERSION}\n'

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_command(self, mock_stdout):
        cmd = ['task-cli', 'salut']
        handle_command(cmd, self.service)
        expected_output = f'{cmd[1]} is not a valid task-cli command\n'

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_command(self, mock_stdout):
        cmd = ['task-cli', 'add', 'salut']
        tasks_count = len(self.service.list_tasks())

        self.assertEqual(tasks_count, 0)

        handle_command(cmd, self.service)
        task_index = self.service.get_task_index(tasks_count + 1)
        self.assertNotEqual(task_index, -1)

        task_data = self.service.list_tasks()[task_index]

        self.assertIsNotNone(task_data)
        self.assertIsInstance(task_data, Task)

        self.assertIn('id', mock_stdout.getvalue())
        self.assertIn('description', mock_stdout.getvalue())
        self.assertIn('status', mock_stdout.getvalue())
        self.assertIn('createdAt', mock_stdout.getvalue())
        self.assertIn('updatedAt', mock_stdout.getvalue())
        self.assertIn(str(task_data.id), mock_stdout.getvalue())
        self.assertIn(task_data.description, mock_stdout.getvalue())
        self.assertIn(task_data.status, mock_stdout.getvalue())
        self.assertEqual(task_data.status, TaskStatus.TODO)
        self.assertIsNotNone(task_data.createdAt)
        self.assertIsNone(task_data.updatedAt)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_command_with_wrong_param(self, mock_stdout):
        cmd = ['task-cli', 'update', '1']
        handle_command(cmd, self.service)
        expected_output = "Usage: task-cli update <task_id> <new_title>\n"

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_command_with_wrong_task_id(self, mock_stdout):
        cmd = ['task-cli', 'update', 'salut', 'salut']
        handle_command(cmd, self.service)
        expected_output = 'Task ID must be an integer\n'

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_update_command_with_good_params(self, mock_stdout):
        cmd = ['task-cli', 'add', 'salut']
        handle_command(cmd, self.service)

        self.assertEqual(len(self.service.list_tasks()), 1)
        self.assertEqual(self.service.list_tasks()[0].description, 'salut')

        cmd2 = ['task-cli', 'update', '1', 'other']
        handle_command(cmd2, self.service)
        task_data = self.service.list_tasks()[0]

        self.assertEqual(len(self.service.list_tasks()), 1)
        self.assertEqual(task_data.description, 'other')
        self.assertIn('id', mock_stdout.getvalue())
        self.assertIn('description', mock_stdout.getvalue())
        self.assertIn('status', mock_stdout.getvalue())
        self.assertIn('createdAt', mock_stdout.getvalue())
        self.assertIn('updatedAt', mock_stdout.getvalue())
        self.assertIn(str(task_data.id), mock_stdout.getvalue())
        self.assertIn(task_data.description, mock_stdout.getvalue())
        self.assertIn(task_data.status, mock_stdout.getvalue())
        self.assertEqual(task_data.status, TaskStatus.TODO)
        self.assertIsNotNone(task_data.createdAt)
        self.assertIsNotNone(task_data.updatedAt)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_delete_command_with_wrong_param(self, mock_stdout):
        cmd = ['task-cli', 'add', 'salut']
        handle_command(cmd, self.service)

        self.assertEqual(len(self.service.list_tasks()), 1)
        self.assertEqual(self.service.list_tasks()[0].description, 'salut')

        cmd = ['task-cli', 'delete', '1', 'salut']
        handle_command(cmd, self.service)
        expected_output = 'Usage: task-cli delete <task_id>\n'

        self.assertIn(expected_output, mock_stdout.getvalue())
        self.assertEqual(len(self.service.list_tasks()), 1)
        self.assertEqual(self.service.list_tasks()[0].description, 'salut')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_delete_command_with_wrong_task_id(self, mock_stdout):
        cmd = ['task-cli', 'add', 'salut']
        handle_command(cmd, self.service)

        self.assertEqual(len(self.service.list_tasks()), 1)
        self.assertEqual(self.service.list_tasks()[0].description, 'salut')

        cmd = ['task-cli', 'delete', 'salut', 'salut']
        handle_command(cmd, self.service)
        expected_output = 'Task ID must be an integer\n'

        self.assertIn(expected_output, mock_stdout.getvalue())
        self.assertEqual(len(self.service.list_tasks()), 1)
        self.assertEqual(self.service.list_tasks()[0].description, 'salut')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_delete_command_with_fake_id(self, mock_stdout):
        cmd = ['task-cli', 'add', 'salut']
        handle_command(cmd, self.service)

        self.assertEqual(len(self.service.list_tasks()), 1)
        self.assertEqual(self.service.list_tasks()[0].description, 'salut')

        cmd = ['task-cli', 'delete', '5']
        handle_command(cmd, self.service)
        self.assertEqual(len(self.service.list_tasks()), 1)
        self.assertEqual(self.service.list_tasks()[0].description, 'salut')

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_delete_command_with_good_params(self, mock_stdout):
        cmd = ['task-cli', 'add', 'salut']
        handle_command(cmd, self.service)

        self.assertEqual(len(self.service.list_tasks()), 1)
        self.assertEqual(self.service.list_tasks()[0].description, 'salut')

        cmd = ['task-cli', 'delete', '1']
        handle_command(cmd, self.service)

        self.assertEqual(len(self.service.list_tasks()), 0)
        self.assertIn('id', mock_stdout.getvalue())
        self.assertIn('description', mock_stdout.getvalue())
        self.assertIn('status', mock_stdout.getvalue())
        self.assertIn('createdAt', mock_stdout.getvalue())
        self.assertIn('updatedAt', mock_stdout.getvalue())

    @unittest.skip("Test temporairement désactivé")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_make_in_progress_status_with_wrong_status(self, mock_stdout):
        cmd = ['task-cli', 'mark-in-progres', 'salut']
        handle_command(cmd, self.service)
        expected_output = 'Task ID must be an integer\n'

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.skip("Test temporairement désactivé")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_make_in_progress_status_with_wrong_params(self, mock_stdout):
        cmd = ['task-cli', 'mark-in-progres', '1', 'salut']
        handle_command(cmd, self.service)
        expected_output = 'Usage: task-cli mark-in-progress <task_id>\n'

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @unittest.skip("Test temporairement désactivé")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_make_in_progress_status_with_good_params(self, mock_stdout):
        cmd = ['task-cli', 'add', 'salut']
        handle_command(cmd, self.service)

        self.assertEqual(len(self.service.list_tasks()), 1)
        self.assertEqual(self.service.list_tasks()[0].id, 1)
        self.assertEqual(self.service.list_tasks()[0].description, 'salut')
        self.assertEqual(self.service.list_tasks()[0].status, TaskStatus.TODO)

        cmd = ['task-cli', 'mark-in-progres', '1']
        handle_command(cmd, self.service)
        task_data = self.service.list_tasks()[0]

        self.assertEqual(len(self.service.list_tasks()), 1)
        self.assertIn('id', mock_stdout.getvalue())
        self.assertIn('description', mock_stdout.getvalue())
        self.assertIn('status', mock_stdout.getvalue())
        self.assertIn('createdAt', mock_stdout.getvalue())
        self.assertIn('updatedAt', mock_stdout.getvalue())
        self.assertIn(str(task_data.id), mock_stdout.getvalue())
        self.assertIn(task_data.description, mock_stdout.getvalue())
        self.assertIn(task_data.status, mock_stdout.getvalue())
        self.assertEqual(task_data.status, TaskStatus.IN_PROGRESS)
        self.assertIsNotNone(task_data.createdAt)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_make_done_status_with_wrong_status(self, mock_stdout):
        cmd = ['task-cli', 'mark-done', 'salut']
        handle_command(cmd, self.service)
        expected_output = 'Task ID must be an integer\n'

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_make_done_status_with_wrong_params(self, mock_stdout):
        cmd = ['task-cli', 'mark-done', '1', 'salut']
        handle_command(cmd, self.service)
        expected_output = 'Usage: task-cli mark-done <task_id>\n'

        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_make_done_status_with_good_params(self, mock_stdout):
        cmd = ['task-cli', 'add', 'salut']
        handle_command(cmd, self.service)

        self.assertEqual(len(self.service.list_tasks()), 1)
        self.assertEqual(self.service.list_tasks()[0].id, 1)
        self.assertEqual(self.service.list_tasks()[0].description, 'salut')
        self.assertEqual(self.service.list_tasks()[0].status, TaskStatus.TODO)

        cmd = ['task-cli', 'mark-done', '1']
        handle_command(cmd, self.service)
        task_data = self.service.list_tasks()[0]

        self.assertEqual(len(self.service.list_tasks()), 1)
        self.assertIn('id', mock_stdout.getvalue())
        self.assertIn('description', mock_stdout.getvalue())
        self.assertIn('status', mock_stdout.getvalue())
        self.assertIn('createdAt', mock_stdout.getvalue())
        self.assertIn('updatedAt', mock_stdout.getvalue())
        self.assertIn(str(task_data.id), mock_stdout.getvalue())
        self.assertIn(task_data.description, mock_stdout.getvalue())
        self.assertIn(task_data.status, mock_stdout.getvalue())
        self.assertEqual(task_data.status, TaskStatus.DONE)
        self.assertIsNotNone(task_data.createdAt)

if __name__ == '__main__':
    unittest.main()

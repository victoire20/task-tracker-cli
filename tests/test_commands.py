import io
import os.path
import unittest
from unittest.mock import patch

from application.task_service import TaskService
from cli.commands import add_commands, list_commands, change_status_commands, update_commands, delete_commands
from domain.entities import TaskStatus
from infrastructure.json_repository import JsonTaskRepository


class TestCommands(unittest.TestCase):
    def setUp(self):
        self.file_path = '../data/test_tasks.json'
        self.repo = JsonTaskRepository(self.file_path)
        self.service = TaskService(self.repo)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_commands(self, mock_stdout):
        add_commands("Test task", self.service)

        self.assertEqual(mock_stdout.getvalue(), f"Task added successfully (ID: {self.service.list_tasks()[0].id})\n")

        add_commands('Encore', self.service)

        self.assertEqual(2, len(self.service.list_tasks()))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_list_commands(self, mock_stdout):
        add_commands("First task", self.service)
        add_commands("Second task", self.service)
        list_commands(self.service)

        self.assertEqual(2, len(self.service.list_tasks()))
        self.assertIn('id', mock_stdout.getvalue())
        self.assertIn('description', mock_stdout.getvalue())
        self.assertIn('First task', mock_stdout.getvalue())
        self.assertIn('Second task', mock_stdout.getvalue())
        self.assertIn('todo', mock_stdout.getvalue())
        self.assertNotIn('Third Task', mock_stdout.getvalue())
        self.assertNotIn('done', mock_stdout.getvalue())
        self.assertNotIn('in-progress', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_list_tasks_done(self, mock_stdout):
        add_commands("First task", self.service)
        add_commands("Second task", self.service)
        change_status_commands(self.service.list_tasks()[0].id, TaskStatus.DONE, self.service)
        list_commands(self.service)

        self.assertEqual(2, len(self.service.list_tasks()))
        self.assertIn('id', mock_stdout.getvalue())
        self.assertIn('description', mock_stdout.getvalue())
        self.assertIn('First task', mock_stdout.getvalue())
        self.assertIn('Second task', mock_stdout.getvalue())
        self.assertIn('todo', mock_stdout.getvalue())
        self.assertIn('done', mock_stdout.getvalue())
        self.assertEqual(self.service.list_tasks()[0].status, TaskStatus.DONE)
        self.assertEqual(self.service.list_tasks()[1].status, TaskStatus.TODO)
        self.assertNotIn('Third Task', mock_stdout.getvalue())
        self.assertNotIn('in-progress', mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_list_tasks_in_progress(self, mock_stdout):
        add_commands("First task", self.service)
        add_commands("Second task", self.service)
        change_status_commands(self.service.list_tasks()[1].id, TaskStatus.IN_PROGRESS, self.service)
        list_commands(self.service)

        self.assertEqual(2, len(self.service.list_tasks()))
        self.assertIn('id', mock_stdout.getvalue())
        self.assertIn('description', mock_stdout.getvalue())
        self.assertIn('First task', mock_stdout.getvalue())
        self.assertIn('Second task', mock_stdout.getvalue())
        self.assertIn('todo', mock_stdout.getvalue())
        self.assertIn('in-progress', mock_stdout.getvalue())
        self.assertEqual(self.service.list_tasks()[0].status, TaskStatus.TODO)
        self.assertEqual(self.service.list_tasks()[1].status, TaskStatus.IN_PROGRESS)
        self.assertNotIn('Third Task', mock_stdout.getvalue())
        self.assertNotIn('done', mock_stdout.getvalue())

    def test_change_status(self):
        add_commands("First task", self.service)

        self.assertEqual(1, len(self.service.list_tasks()))
        self.assertEqual(self.service.list_tasks()[0].status, TaskStatus.TODO)

        change_status_commands(self.service.list_tasks()[0].id, TaskStatus.IN_PROGRESS, self.service)

        self.assertEqual(1, len(self.service.list_tasks()))
        self.assertEqual(self.service.list_tasks()[0].status, TaskStatus.IN_PROGRESS)

        change_status_commands(self.service.list_tasks()[0].id, TaskStatus.DONE, self.service)

        self.assertEqual(1, len(self.service.list_tasks()))
        self.assertEqual(self.service.list_tasks()[0].status, TaskStatus.DONE)

    def test_update_task(self):
        add_commands("First task", self.service)

        self.assertEqual(1, len(self.service.list_tasks()))
        self.assertEqual(self.service.list_tasks()[0].id, 1)
        self.assertEqual(self.service.list_tasks()[0].description, "First task")

        update_commands(1, 'new description', self.service)

        self.assertEqual(1, len(self.service.list_tasks()))
        self.assertEqual(self.service.list_tasks()[0].id, 1)
        self.assertEqual(self.service.list_tasks()[0].description, 'new description')

    def test_delete_task(self):
        add_commands("First task", self.service)
        add_commands("Second task", self.service)

        self.assertEqual(2, len(self.service.list_tasks()))
        self.assertEqual(self.service.list_tasks()[0].id, 1)
        self.assertEqual(self.service.list_tasks()[0].description, "First task")

        delete_commands(1, self.service)

        self.assertEqual(1, len(self.service.list_tasks()))
        self.assertEqual(self.service.list_tasks()[0].id, 2)
        self.assertEqual(self.service.list_tasks()[0].description, "Second task")


if __name__ == '__main__':
    unittest.main()

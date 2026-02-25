import os.path
import unittest

from application.task_service import TaskService
from domain.entities import Task, TaskStatus
from infrastructure.json_repository import JsonTaskRepository


class TestTaskService(unittest.TestCase):
    def setUp(self):
        self.file_path = '../data/test_tasks.json'
        self.repository = JsonTaskRepository(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_add_task_service(self):
        task_service = TaskService(self.repository)
        new_task = task_service.add_task(description="Task 1")

        self.assertEqual(1, len(self.repository.load()))
        self.assertEqual(new_task, 1)

    def test_list_tasks(self):
        task_service = TaskService(self.repository)
        task_service.add_task(description="Task 1")
        task_service.add_task(description="Task 2")

        self.assertEqual(2, len(task_service.list_tasks()))
        self.assertIsInstance(task_service.list_tasks(), list)
        self.assertIsInstance(task_service.list_tasks()[0], Task)
        self.assertEqual(task_service.list_tasks()[0].id, 1)
        self.assertEqual(task_service.list_tasks()[0].description, 'Task 1')
        self.assertEqual(task_service.list_tasks()[0].status, TaskStatus.TODO)
        self.assertIsInstance(task_service.list_tasks()[1], Task)
        self.assertEqual(task_service.list_tasks()[1].id, 2)
        self.assertEqual(task_service.list_tasks()[1].description, 'Task 2')
        self.assertEqual(task_service.list_tasks()[1].status, TaskStatus.TODO)

    def test_change_task_status(self):
        task_service = TaskService(self.repository)
        task_service.add_task(description="Task 1")

        self.assertEqual(1 , len(task_service.list_tasks()))
        self.assertEqual(task_service.list_tasks()[0].id, 1)
        self.assertEqual(task_service.list_tasks()[0].description, 'Task 1')
        self.assertEqual(task_service.list_tasks()[0].status, TaskStatus.TODO)

        task_service.change_task_status(task_service.list_tasks()[0].id, TaskStatus.IN_PROGRESS)
        task_index = task_service.get_task_index(task_service.list_tasks()[0].id)

        self.assertEqual(1 , len(task_service.list_tasks()))
        self.assertEqual(task_service.list_tasks()[0].id, 1)
        self.assertEqual(task_service.list_tasks()[0].description, 'Task 1')
        self.assertEqual(task_service.list_tasks()[task_index].status, TaskStatus.IN_PROGRESS)

        task_service.change_task_status(task_service.list_tasks()[0].id, TaskStatus.DONE)

        self.assertEqual(1 , len(task_service.list_tasks()))
        self.assertEqual(task_service.list_tasks()[0].id, 1)
        self.assertEqual(task_service.list_tasks()[0].description, 'Task 1')
        self.assertEqual(task_service.list_tasks()[task_index].status, TaskStatus.DONE)

    def test_list_tasks_with_status_done(self):
        task_service = TaskService(self.repository)
        task_service.add_task(description="Task 1")
        task_service.add_task(description="Task 2")
        task_service.change_task_status(1, TaskStatus.DONE)

        self.assertEqual(1, len(task_service.list_tasks(TaskStatus.DONE)))
        self.assertIsInstance(task_service.list_tasks(), list)
        self.assertIsInstance(task_service.list_tasks()[0], Task)
        self.assertEqual(task_service.list_tasks()[0].id, 1)
        self.assertEqual(task_service.list_tasks()[0].description, 'Task 1')
        self.assertEqual(task_service.list_tasks()[0].status, TaskStatus.DONE)
        self.assertIsInstance(task_service.list_tasks()[1], Task)
        self.assertEqual(task_service.list_tasks()[1].id, 2)
        self.assertEqual(task_service.list_tasks()[1].description, 'Task 2')
        self.assertEqual(task_service.list_tasks()[1].status, TaskStatus.TODO)

    def test_list_tasks_with_status_todo(self):
        task_service = TaskService(self.repository)
        task_service.add_task(description="Task 1")
        task_service.add_task(description="Task 2")
        task_service.change_task_status(1, TaskStatus.DONE)
        task_service.change_task_status(2, TaskStatus.IN_PROGRESS)

        self.assertEqual(0, len(task_service.list_tasks(TaskStatus.TODO)))
        self.assertIsInstance(task_service.list_tasks(), list)
        self.assertIsInstance(task_service.list_tasks()[0], Task)
        self.assertEqual(task_service.list_tasks()[0].id, 1)
        self.assertEqual(task_service.list_tasks()[0].description, 'Task 1')
        self.assertEqual(task_service.list_tasks()[0].status, TaskStatus.DONE)
        self.assertIsInstance(task_service.list_tasks()[1], Task)
        self.assertEqual(task_service.list_tasks()[1].id, 2)
        self.assertEqual(task_service.list_tasks()[1].description, 'Task 2')
        self.assertEqual(task_service.list_tasks()[1].status, TaskStatus.IN_PROGRESS)

    def test_list_tasks_with_status_in_progress(self):
        task_service = TaskService(self.repository)
        task_service.add_task(description="Task 1")
        task_service.add_task(description="Task 2")
        task_service.change_task_status(1, TaskStatus.IN_PROGRESS)
        task_service.change_task_status(2, TaskStatus.IN_PROGRESS)

        self.assertEqual(2, len(task_service.list_tasks(TaskStatus.IN_PROGRESS)))
        self.assertIsInstance(task_service.list_tasks(), list)
        self.assertIsInstance(task_service.list_tasks()[0], Task)
        self.assertEqual(task_service.list_tasks()[0].id, 1)
        self.assertEqual(task_service.list_tasks()[0].description, 'Task 1')
        self.assertEqual(task_service.list_tasks()[0].status, TaskStatus.IN_PROGRESS)
        self.assertIsInstance(task_service.list_tasks()[1], Task)
        self.assertEqual(task_service.list_tasks()[1].id, 2)
        self.assertEqual(task_service.list_tasks()[1].description, 'Task 2')
        self.assertEqual(task_service.list_tasks()[1].status, TaskStatus.IN_PROGRESS)

    def test_get_task_by_id(self):
        task_service = TaskService(self.repository)
        task_service.add_task(description="Task 1")
        task_service.add_task(description="Task 2")
        task_index = task_service.get_task_index(2)

        self.assertEqual(2, len(task_service.list_tasks()))
        self.assertEqual(task_index, 1)
        self.assertEqual(task_service.list_tasks()[task_index].id, 2)
        self.assertEqual(task_service.list_tasks()[task_index].description, 'Task 2')

    def test_get_task_by_id_with_fake_id(self):
        task_service = TaskService(self.repository)
        task_service.add_task(description="Task 1")
        task_index = task_service.get_task_index(2)

        self.assertEqual(task_index, -1)
        self.assertEqual(1, len(task_service.list_tasks()))

    def test_update_task(self):
        task_service = TaskService(self.repository)
        task_service.add_task(description="Task 1")

        self.assertEqual(1, len(task_service.list_tasks()))
        self.assertEqual(task_service.list_tasks()[0].id, 1)
        self.assertEqual(task_service.list_tasks()[0].description, 'Task 1')
        self.assertEqual(task_service.list_tasks()[0].status, TaskStatus.TODO)
        self.assertIsNone(task_service.list_tasks()[0].updatedAt)

        task_service.update_task(task_id=1, description='New description')

        self.assertEqual(1, len(task_service.list_tasks()))
        self.assertEqual(task_service.list_tasks()[0].id, 1)
        self.assertEqual(task_service.list_tasks()[0].description, 'New description')
        self.assertEqual(task_service.list_tasks()[0].status, TaskStatus.TODO)
        self.assertIsNotNone(task_service.list_tasks()[0].updatedAt)

    def test_delete_task(self):
        task_service = TaskService(self.repository)
        task_service.add_task(description="Task 1")
        task_service.add_task(description="Task 2")

        self.assertEqual(2, len(task_service.list_tasks()))
        self.assertEqual(task_service.list_tasks()[0].description, 'Task 1')

        task_service.delete_task(1)

        self.assertEqual(1, len(task_service.list_tasks()))
        self.assertEqual(task_service.list_tasks()[0].description, 'Task 2')


if __name__ == '__main__':
    unittest.main()

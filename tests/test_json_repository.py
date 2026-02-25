import json
import os
import unittest
from datetime import datetime
from pathlib import Path

from domain.entities import Task, TaskStatus
from infrastructure.json_repository import JsonTaskRepository


class TestJsonTaskRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.file_path = '../data/test_tasks.json'
        self.date = str(datetime.now())

    def tearDown(self) -> None:
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_load_with_file_not_exist(self):
        f = JsonTaskRepository(self.file_path)
        tasks_list = f.load()
        self.assertEqual(tasks_list, [])
        self.assertEqual(len(tasks_list), 0)
        self.assertIsInstance(tasks_list, list)
        self.assertEqual(Path(self.file_path).exists(), True)

    def test_load_with_file_is_empty(self):
        self.file_path = '../data/tasks.json'
        f = JsonTaskRepository(self.file_path)
        tasks_list = f.load()
        self.assertEqual(tasks_list, [])
        self.assertEqual(len(tasks_list), 0)
        self.assertIsInstance(tasks_list, list)
        self.assertEqual(Path(self.file_path).exists(), True)

    def test_load_with_data(self):
        f = JsonTaskRepository(self.file_path)
        Path(self.file_path).write_text(json.dumps(
            [Task(id=1, description="test", status=TaskStatus.TODO, createdAt=self.date).__dict__]
        ))
        all_tasks = f.load()
        self.assertEqual(len(all_tasks), 1)
        self.assertIsInstance(all_tasks, list)
        self.assertIsInstance(all_tasks[0], Task)
        self.assertEqual(all_tasks[0].id, 1)
        self.assertEqual(all_tasks[0].description, 'test')
        self.assertEqual(all_tasks[0].status, TaskStatus.TODO)
        self.assertEqual(all_tasks[0].createdAt, self.date)
        self.assertIsNone(all_tasks[0].updatedAt)
        self.assertEqual(Path(self.file_path).exists(), True)

    def test_save_empty_data_in_file(self):
        f = JsonTaskRepository(self.file_path)

        self.assertEqual(len(f.load()), 0)

        f.save([Task(id=1, description="test", status=TaskStatus.TODO, createdAt=self.date)])

        self.assertEqual(len(f.load()), 1)
        self.assertEqual(Path(self.file_path).exists(), True)


if __name__ == '__main__':
    unittest.main()

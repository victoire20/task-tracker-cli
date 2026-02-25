import unittest

from main import create_task, Task, get_task_by_id, update_task_by_id


class MyTestCase(unittest.TestCase):
    def test_create_new_task(self):
        new_task = create_task(description="Task description")
        self.assertIsInstance(new_task, Task)
        self.assertEqual(new_task.id, 1)
        #self.assertEqual(new_task[1], f"Task added successfully (ID: {new_task["id"]})")

    def test_get_task_by_id(self):
        task = get_task_by_id(1)
        self.assertIsNotNone(task)
        self.assertIsInstance(task, int)
        #self.assertEqual(task, 1)

    def test_update_task_by_id(self):
        task = update_task_by_id(1, 'another description')
        pass

    def test_delete_task_by_id(self):
        task = get_task_by_id(1)
        self.assertIsNone(task)


if __name__ == '__main__':
    unittest.main()

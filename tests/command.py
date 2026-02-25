import unittest

from main import create_task, Task


class MyTestCase(unittest.TestCase):
    def test_create_new_task(self):
        new_task = create_task(description="Task description")
        self.assertEqual(isinstance(new_task, Task), True)
        self.assertEqual(new_task.id, 1)
        #self.assertEqual(new_task[1], f"Task added successfully (ID: {new_task["id"]})")


if __name__ == '__main__':
    unittest.main()

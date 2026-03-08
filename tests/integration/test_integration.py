import os
import subprocess
import unittest


class TestIntegration(unittest.TestCase):
    def setUp(self):
        BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

        self.data_dir = os.path.join(BASE_DIR, 'data')
        self.file_path = os.path.join(self.data_dir, 'test_tasks.json')

        os.makedirs(self.data_dir, exist_ok=True)

        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_add_command(self):
        result = subprocess.run(
            ["task-cli", "add", "Buy milk"],
            cwd=self.data_dir,
            capture_output=True,
            text=True
        )

        self.assertEqual(result.returncode, 0)
        print(f"file exist : {os.path.exists(self.file_path)}")

        # Vérifie le contenu
        #with open(self.file_path, 'r') as f:
        #    tasks = json.load(f)

        #self.assertEqual(len(tasks), 1)
        #self.assertEqual(tasks[0]['description'], 'Buy a book')
        #self.assertEqual(tasks[0]['status'], 'todo')


if __name__ == '__main__':
    unittest.main()

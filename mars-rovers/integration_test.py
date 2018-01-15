import unittest
import subprocess

class IntegrationTest(unittest.TestCase):
    def test_input(self):
        completed_process = subprocess.run(["python3", "./mars_rovers.py"], stdout = subprocess.PIPE, input='5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM', encoding='ascii')
        self.assertEqual(completed_process.returncode, 0)

        self.assertEqual("1 3 N\n5 1 E\n", completed_process.stdout)

if __name__ == '__main__':
    unittest.main()

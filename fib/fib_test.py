import unittest
from fib import fib

class FibTest(unittest.TestCase):
    def test_0(self):
        self.assertEqual(fib(0), 0)

    def test_1(self):
        self.assertEqual(fib(1), 1)

    def test_2(self):
        self.assertEqual(fib(2), 1)

    def test_3(self):
        self.assertEqual(fib(3), 2)

    def test_4(self):
        self.assertEqual(fib(4), 3)

    def test_5(self):
        self.assertEqual(fib(5), 5)

    def test_10(self):
        self.assertEqual(fib(10), 55)

    def test_30(self):
        self.assertEqual(fib(30), 832040)

if __name__ == '__main__':
    unittest.main()

import unittest
from Assignment5NickT import FToC
from Assignment5NickT import Fibonacci
class TestAssignment5(unittest.TestCase):
    def test_FtoC(self):
        self.assertEqual(FToC(32), 0)
        self.assertEqual(FToC(212), 100)
    
    def test_Fibonacci(self):
        self.assertEqual(Fibonacci(10), 55)
        self.assertEqual(Fibonacci(0), 0)
        self.assertEqual(Fibonacci(1), 1)

if __name__ == "__main__":
    unittest.main()
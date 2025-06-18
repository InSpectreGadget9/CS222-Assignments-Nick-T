import unittest
from Assignment6NickT import add
from Assignment6NickT import subtract
from Assignment6NickT import multiply
from Assignment6NickT import division
class TestAssignment6(unittest.TestCase):
    def test_Add(self):
        self.assertEqual(add(2,2), 4)
        self.assertEqual(add(-2,-3), -5)
        self.assertEqual(add(0,4), 4)
        self.assertEqual(add(-1,2), 1)
        self.assertEqual(add(-2,1), -1)
    
    def test_Subtract(self):
        self.assertEqual(subtract(2,2), 0)
        self.assertEqual(subtract(-3,4), -7)
        self.assertEqual(subtract(-3,-3), 0)
        self.assertEqual(subtract(-5, -4), -1)

    def test_Multiply(self):
        self.assertEqual(multiply(2,2), 4)
        self.assertEqual(multiply(2,0), 0)
        self.assertEqual(multiply(2,1), 2)
        self.assertEqual(multiply(2,-2), -4)
        self.assertEqual(multiply(-3,3), -9)
        self.assertEqual(multiply(-2,-2), 4)

    def test_Divide(self):
        self.assertEqual(division(2,2), 1)
        self.assertEqual(division(0,2), 0)
        self.assertEqual(division(2,0), 0)

if __name__ == "__main__":
    unittest.main()
        
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
    def test_add2(self):
        self.assertEqual(self.calc.add(5, -2), 3)    
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 2), 3)
    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(5, -2), 7)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(6, 2), 12)
    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(3, -6), -18)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8, 2), 4)
    def test_divide2(self):
        self.assertEqual(self.calc.divide(8, -2), -4)
    def test_divide3(self):
        self.assertEqual(self.calc.divide(8, 0),"Undefined")

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(9, 2), 1)
    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(5,0),"Undefined")
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()
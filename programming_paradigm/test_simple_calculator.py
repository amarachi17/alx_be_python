import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        # Set up the simple calculator instance before each test
        self.calc = SimpleCalculator()
        
    def test_addition(self):
        # Test the addition operation
        self.assertEqual(self.calc.add(2, 3),5)
        self.assertEqual(self.calc.add(-1, 1),0)
        self.assertEqual(self.calc.add(0, 0),0)
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
    
    def test_subtraction(self):
        # Test the subtraction operation
        self.assertEqual(self.calc.subtract(5, 3),2)
        self.assertEqual(self.calc.subtract(0, 5),-5)
        self.assertEqual(self.calc.subtract(-5, -3),-2)
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0)
        
    def test_multiplication(self):
        # Test the multiplication operation
        self.assertEqual(self.calc.multiply(2, 3),6)
        self.assertEqual(self.calc.multiply(-1, 5),-5)
        self.assertEqual(self.calc.multiply(0, 100),0)
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)
        
    def test_division(self):
        # Test the division operation
        self.assertEqual(self.calc.divide(6, 3),2)
        self.assertEqual(self.calc.divide(-6, 2),-3)
        self.assertEqual(self.calc.divide(0, 1),0)
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        
        # Test division by zero
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        
if __name__ == '__main__':
    unittest.main()
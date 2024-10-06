import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(4, 6), 10)
        # Add more assertions to thoroughly test the add method.

    def test_subtract(self):
        """"test the subtract method"""
        self.assertEqual(self.calc.subtract(5, 3), 2) 
        self.assertEqual(self.calc.subtract(7, 6), 1) 

    def test_multiply(self):
        """"test the multiply method""" 
        self.assertEqual(self.calc.multiply(3, 7), 21)
        self.assertEqual(self.calc.multiply(4, 4), 16) 

    def test_divide(self):
        """"test the divide method"""   
        self.assertEqual(self.calc.divide(6, 3), 2)   
        self.assertEqual(self.calc.divide(9, 3), 3)

        #test division by zero
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)  
if __name__ == "__main__":
    unittest.main()       
import unittest
import math

class TestCalculator(unittest.TestCase):

    def test_square_root(self):
        self.assertEqual(math.sqrt(16), 4)

    def test_power(self):
        self.assertEqual(pow(2,3), 8)

    def test_factorial(self):
        self.assertEqual(math.factorial(5), 120)

    def test_log(self):
        self.assertAlmostEqual(math.log(10), 2.302585, places=3)

if __name__ == '__main__':
    unittest.main()

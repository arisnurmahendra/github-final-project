import unittest
from shipping_calculator import calculate_shipping_cost, calculate_tax

class TestShippingCalculator(unittest.TestCase):
    def test_calculate_shipping_cost(self):
        cost = calculate_shipping_cost(10, 100, "truck")
        self.assertEqual(cost, 25.4)  # 5 + (10*2) + (100*0.1) + 8% tax

    def test_calculate_tax(self):
        tax = calculate_tax(100)
        self.assertEqual(tax, 8.0)  # 8% of 100

if __name__ == '__main__':
    unittest.main()

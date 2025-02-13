import unittest

from src.adapters.SimpleSuperStock import SimpleSuperStocks, TEA
from src.adapters.SimpleSuperStock import SimpleSuperStocks, TEA, GIN

class TestSimpleSuperStock(unittest.TestCase):

    def setUp(self):
        self.stock = SimpleSuperStocks(150.0, "AAPL")

    def test_price(self):
        self.assertEqual(self.stock.price, 150.0)

    def test_stock_symbol(self):
        self.assertEqual(self.stock.stock_symbol, "AAPL")

    def test_yield(self):
        self.assertEqual(self.stock.calculate_yield(), None)

class TestTEAStock(unittest.TestCase):

    def setUp(self):
        self.stock = TEA(100.0, "TEA")

    def test_price(self):
        self.assertEqual(self.stock.price, 100.0)

    def test_stock_symbol(self):
        self.assertEqual(self.stock.stock_symbol, "TEA")

    def test_yield(self):
        self.assertEqual(self.stock.calculate_yield(), 0.0)

    def test_pe_ratio(self):
        with self.assertRaises(ZeroDivisionError):
            self.stock.calculate_pe_ratio()

class TestGINStock(unittest.TestCase):

    def setUp(self):
        self.stock = GIN(200.0, "GIN")

    def test_price(self):
        self.assertEqual(self.stock.price, 200.0)

    def test_stock_symbol(self):
        self.assertEqual(self.stock.stock_symbol, "GIN")

    def test_yield(self):
        self.assertEqual(self.stock.calculate_yield(), 0.01)

    def test_pe_ratio(self):
        self.assertEqual(self.stock.calculate_pe_ratio(), 200.0 / 2.0)

if __name__ == '__main__':
    unittest.main()
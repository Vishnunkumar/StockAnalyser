from src.adapters.SimpleSuperStock import StockFactory

stock_factory = StockFactory.get_stock_factory()

class Validator:
    def __init__(self):
        pass

    def stock_validator(self, stock_symbol):
        if stock_symbol in stock_factory.keys():
            pass
        else:
            raise(Exception("Invalid stock symbol"))
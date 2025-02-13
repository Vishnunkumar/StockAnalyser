
class SimpleSuperStocks:
    def __init__(self, price: float, stock_symbol: str):
        self.price = price
        self.stock_symbol = stock_symbol
    
    def calculate_yield(self):
        pass

    def calculate_pe_ratio(self):
        pass


class CommonStock(SimpleSuperStocks):
    def calculate_yield(self):
        return self.dividend / self.price

    def calculate_pe_ratio(self):
        return self.price / self.dividend
    
    
class PreferredStock(SimpleSuperStocks):
    def calculate_yield(self):
        return (self.fixed_dividend * self.par_value) / self.price

    def calculate_pe_ratio(self):
        return self.price / (self.fixed_dividend * self.par_value)
    

class TEA(CommonStock):
    dividend = 0
    
    def calculate_yield(self):
        return self.dividend / self.price

    def calculate_pe_ratio(self):
        return self.price / self.dividend
    

class POP(CommonStock):
    dividend = 8
    
    def calculate_yield(self):
        return self.dividend / self.price

    def calculate_pe_ratio(self):
        return self.price / self.dividend
    
class ALE(CommonStock):
    dividend = 23

    def calculate_yield(self): 
        return self.dividend / self.price
    
    def calculate_pe_ratio(self):
        return self.price / self.dividend
    
class GIN(PreferredStock):
    fixed_dividend = 0.02
    par_value = 100

    def calculate_yield(self):
        return (self.fixed_dividend * self.par_value) / self.price
    
    def calculate_pe_ratio(self):
        return self.price / (self.fixed_dividend * self.par_value)
    
class JOE(CommonStock):
    dividend = 13

    def calculate_yield(self):
        return self.dividend / self.price

    def calculate_pe_ratio(self):
        return self.price / self.dividend
    

class StockFactory:

    @staticmethod
    def get_stock_factory():
        return {
            "TEA": TEA,
            "POP": POP,
            "ALE": ALE,
            "GIN": GIN,
            "JOE": JOE
        }    
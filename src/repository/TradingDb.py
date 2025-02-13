import datetime

class TradingDataStore:
    def __init__(self):
        self.tables = {}

    def create_table(self, table_name, columns):
        if table_name in self.tables:
            print(f"Table {table_name} already exists.")
            return

        self.tables[table_name] = {
            "columns": columns,
            "data": []
        }

    def insert_record(self, table_name, record):
        
        if table_name not in self.tables:
            print(f"Table {table_name} does not exist.")
            return

        table_columns = self.tables[table_name]["columns"]
        if set(record.keys()) != set(table_columns):
            print(
                f"Record keys do not match table columns. Expected: {table_columns}, Got: {list(record.keys())}"
            )
            return

        self.tables[table_name]["data"].append(record)

    def query_table(self, table_name, condition=None):
        
        if table_name not in self.tables:
            print(f"Table {table_name} does not exist.")
            return None

        data = self.tables[table_name]["data"]

        if condition:
            return [record for record in data if condition(record)]
        else:
            return data

    def delete_table(self, table_name):
        
        if table_name in self.tables:
            del self.tables[table_name]
            print(f"Table {table_name} deleted.")
        else:
            print(f"Table {table_name} does not exist.")


class TradingMetrics:
    def __init__(self, stock_symbol, trade_data):
        self.stock_symbol = stock_symbol
        self.trade_data = trade_data
    
    def calculate_volume_weighted_stock_price(self):
        time_interval = 5

        current_time = datetime.datetime.now()
        start_time = current_time - datetime.timedelta(minutes=time_interval)
        
        required_trade_data = self.trade_data.query_table(
            "trades",
            condition=lambda record: record["stock_symbol"] == self.stock_symbol
            and record["trade_time"] >= start_time and record["trade_time"] <= current_time
        )

        sum_of_prices = sum([record["stock_price"]*record["trade_quantity"] for record in required_trade_data])
        sum_of_quantities = sum([record["trade_quantity"] for record in required_trade_data])

        return sum_of_prices/sum_of_quantities if sum_of_quantities != 0 else 0.0

    def calculate_all_share_index(self):
        all_trade_data = self.trade_data.query_table("all_share_index")
        product_of_prices = 1
        for record in all_trade_data:
            product_of_prices *= record["weighted_stock_price"]
        return product_of_prices**(1/len(all_trade_data))
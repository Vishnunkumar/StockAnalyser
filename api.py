import uvicorn
import datetime
from typing import Optional
from fastapi import FastAPI, logger
from pydantic import BaseModel
from src.repository.TradingDb import TradingDataStore, TradingMetrics
from src.adapters.SimpleSuperStock import StockFactory
from src.utilities.Validation import Validator
from src.exceptions.ExceptionHandler import ClientException

app = FastAPI()

class StockItem(BaseModel):
    stock_symbol : str
    stock_price : float

class StockResponse(BaseModel):
    status: str
    value: float
    message: str

class TradeRequest(BaseModel):
    stock_symbol : str
    stock_price : Optional[float]
    trade_time : Optional[datetime.datetime]
    trade_quantity : Optional[int]
    trade_indicator : Optional[str]


stock_factory = StockFactory.get_stock_factory()
validator = Validator()
trading_db_instance = TradingDataStore()
trading_db_instance.create_table(
    "trades",
    ["stock_symbol", "stock_price", "trade_time", "trade_quantity", "trade_indicator"]
    )


@app.post("/stocks/get-dividend/")
async def get_dividend(stock_item: StockItem):
    
    try:
        validator.stock_validator(stock_item.stock_symbol)
        stock = stock_factory[stock_item.stock_symbol](stock_item.stock_price, stock_item.stock_symbol)
        logger.logger.info(f"Retrieved Stock: {stock_item.stock_symbol}")
        dividend = stock.calculate_yield()
        
        return StockResponse(
            status="success",
            value=round(dividend, 3),
            message="Yield calculated successfully"
        )

    except Exception as exception:
        logger.logger.error(f"caught runtime exception while processing stock {stock_item.stock_symbol}" + 
                            f"with the following error message {str(exception)}")
        return StockResponse(
            status="error",
            value=0.0,
            message=ClientException(exception).get_exception_message()
        )


@app.post("/stocks/get-pe-ratio/")
async def get_dividend(stock_item: StockItem):
    
    try:
        validator.stock_validator(stock_item.stock_symbol)
        stock = stock_factory[stock_item.stock_symbol](stock_item.stock_price, stock_item.stock_symbol)
        logger.logger.info(f"Retrieved Stock: {stock_item.stock_symbol}")
        pe_ratio = stock.calculate_pe_ratio()
        
        return StockResponse(
            status="success",
            value=round(pe_ratio, 3),
            message="PE ratio calculated successfully"
        )

    except Exception as exception:
        logger.logger.error(f"caught runtime exception while processing stock {stock_item.stock_symbol}" + 
                            f"with the following error message {str(exception)}")
        return StockResponse(
            status="error",
            value=0.0,
            message=ClientException(exception).get_exception_message()
        )

@app.post("/trade/record-trade/")
async def record_trade(trade_details: TradeRequest):
    
    try:
        trade_data = trade_details.dict()
        validator.stock_validator(trade_details.stock_symbol)
        trading_db_instance.insert_record("trades", trade_data)
        logger.logger.info(f"Recorded trade for stock: {trade_details.stock_symbol}")
        
        return StockResponse(
            status="success",
            value=0.0,
            message="Trade recorded successfully"
        )

    except Exception as exception:
        logger.logger.error(f"caught runtime exception while processing trade for stock {trade_details.stock_symbol}" + 
                            f"with the following error message {str(exception)}")
        return StockResponse(
            status="error",
            value=0.0,
            message=ClientException(exception).get_exception_message()
        )
    
@app.post("/trade/get-volume-weighted-stock-price/")
async def get_volume_weighted_stock_price(trade_details: TradeRequest):
    
    try:
        validator.stock_validator(trade_details.stock_symbol)
        trading_metrics = TradingMetrics(trade_details.stock_symbol, trading_db_instance)
        volume_weighted_stock_price = trading_metrics.calculate_volume_weighted_stock_price()
        
        return StockResponse(
            status="success",
            value=round(volume_weighted_stock_price, 3),
            message="Volume weighted stock price calculated successfully"
        )

    except Exception as exception:
        logger.logger.error(f"caught runtime exception while processing stock {trade_details.stock_symbol}" + 
                            f"with the following error message {str(exception)}")
        return StockResponse(
            status="error",
            value=0.0,
            message=ClientException(exception).get_exception_message()
        )
 
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
import pytest
from fastapi.testclient import TestClient
from api import app, StockItem, TradeRequest

client = TestClient(app)

def test_get_dividend_success():
    stock_response = client.post(
        "/stocks/get-dividend/",
        json={"stock_symbol": "TEA", "stock_price": 150.0}
    )
    assert stock_response.status_code == 200
    assert stock_response.json()["status"] == "success"
    assert "value" in stock_response.json()
    assert "message" in stock_response.json()

def test_get_dividend_failure():
    stock_response = client.post(
        "/stocks/get-dividend/",
        json={"stock_symbol": "INVALID", "stock_price": 150.0}
    )
    assert stock_response.status_code == 200
    assert stock_response.json()["status"] == "error"
    assert stock_response.json()["value"] == 0.0
    assert "message" in stock_response.json()

def test_get_pe_ratio_success():
    stock_response = client.post(
        "/stocks/get-pe-ratio/",
        json={"stock_symbol": "GIN", "stock_price": 150.0}
    )
    assert stock_response.status_code == 200
    assert stock_response.json()["status"] == "success"
    assert "value" in stock_response.json()
    assert "message" in stock_response.json()

def test_get_pe_ratio_failure():
    stock_response = client.post(
        "/stocks/get-pe-ratio/",
        json={"stock_symbol": "INVALID", "stock_price": 150.0}
    )
    assert stock_response.status_code == 200
    assert stock_response.json()["status"] == "error"
    assert stock_response.json()["value"] == 0.0
    assert "message" in stock_response.json()

def test_record_trade_success():
    stock_response = client.post(
        "/trade/record-trade/",
        json={
            "stock_symbol": "JOE",
            "stock_price": 150.0,
            "trade_time": "2023-10-10T10:00:00",
            "trade_quantity": 10,
            "trade_indicator": "BUY"
        }
    )
    assert stock_response.status_code == 200
    assert stock_response.json()["status"] == "success"
    assert stock_response.json()["value"] == 0.0
    assert stock_response.json()["message"] == "Trade recorded successfully"

def test_record_trade_failure():
    stock_response = client.post(
        "/trade/record-trade/",
        json={
            "stock_symbol": 2,
            "stock_price": 150.0,
            "trade_time": "2023-10-10T10:00:00",
            "trade_quantity": 10,
            "trade_indicator": "BUY"
        }
    )
    print(stock_response.json())
    assert stock_response.status_code == 200
    assert stock_response.json()["status"] == "error"
    assert stock_response.json()["value"] == 0.0
    assert "message" in stock_response.json()

def test_get_volume_weighted_stock_price_success():
    stock_response = client.post(
        "/trade/get-volume-weighted-stock-price/",
        json={"stock_symbol": "TEA"}
    )
    assert stock_response.status_code == 200
    assert stock_response.json()["status"] == "success"
    assert "value" in stock_response.json()
    assert "message" in stock_response.json()

def test_get_volume_weighted_stock_price_failure():
    stock_response = client.post(
        "/trade/get-volume-weighted-stock-price/",
        json={"stock_symbol": "INVALID"}
    )
    assert stock_response.status_code == 200
    assert stock_response.json()["status"] == "error"
    assert stock_response.json()["value"] == 0.0
    assert "message" in stock_response.json()
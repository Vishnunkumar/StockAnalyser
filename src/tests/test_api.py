import pytest
from fastapi.testclient import TestClient
from api import app, StockItem, TradeRequest

client = TestClient(app)

def test_get_dividend_success():
    response = client.post(
        "/stocks/get-dividend/",
        json={"stock_symbol": "TEA", "stock_price": 150.0}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "value" in response.json()
    assert "message" in response.json()

def test_get_dividend_failure():
    response = client.post(
        "/stocks/get-dividend/",
        json={"stock_symbol": "INVALID", "stock_price": 150.0}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "error"
    assert response.json()["value"] == 0.0
    assert "message" in response.json()

def test_get_pe_ratio_success():
    response = client.post(
        "/stocks/get-pe-ratio/",
        json={"stock_symbol": "GIN", "stock_price": 150.0}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "value" in response.json()
    assert "message" in response.json()

def test_get_pe_ratio_failure():
    response = client.post(
        "/stocks/get-pe-ratio/",
        json={"stock_symbol": "INVALID", "stock_price": 150.0}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "error"
    assert response.json()["value"] == 0.0
    assert "message" in response.json()

def test_record_trade_success():
    response = client.post(
        "/trade/record-trade/",
        json={
            "stock_symbol": "JOE",
            "stock_price": 150.0,
            "trade_time": "2023-10-10T10:00:00",
            "trade_quantity": 10,
            "trade_indicator": "BUY"
        }
    )
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert response.json()["value"] == 0.0
    assert response.json()["message"] == "Trade recorded successfully"

def test_record_trade_failure():
    response = client.post(
        "/trade/record-trade/",
        json={
            "stock_symbol": 2,
            "stock_price": 150.0,
            "trade_time": "2023-10-10T10:00:00",
            "trade_quantity": 10,
            "trade_indicator": "BUY"
        }
    )
    print(response.json())
    assert response.status_code == 200
    assert response.json()["status"] == "error"
    assert response.json()["value"] == 0.0
    assert "message" in response.json()

def test_get_volume_weighted_stock_price_success():
    response = client.post(
        "/trade/get-volume-weighted-stock-price/",
        json={"stock_symbol": "TEA"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "success"
    assert "value" in response.json()
    assert "message" in response.json()

def test_get_volume_weighted_stock_price_failure():
    response = client.post(
        "/trade/get-volume-weighted-stock-price/",
        json={"stock_symbol": "INVALID"}
    )
    assert response.status_code == 200
    assert response.json()["status"] == "error"
    assert response.json()["value"] == 0.0
    assert "message" in response.json()
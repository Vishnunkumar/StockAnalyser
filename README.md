# StockAnalyser
## Overview
StockAnalyser is a comprehensive tool designed to assist investors with basic calculations of metrics and indicators

## Features
- Analysis of historical stock data
- Real-time tracking of stock prices

## Installation
To install StockAnalyser, clone the repository and install the necessary dependencies:
```bash
git clone https://github.com/yourusername/StockAnalyser.git
cd StockAnalyser
pip install -r requirements.txt
```

## Usage
To begin using StockAnalyser, execute the following command:
```bash
uvicorn api:app.py --reload
```
To see how can the API be used, please look into the docs: http://localhost:8000/docs. 

### Problem Statement

- We can integrate SimpleSuperStock directly as a code object to any existing feature, it helps getting the below information based on a
given stock 
    - to get dividend : example: call 
    - to get PE ratio
- TradingDatastore acts as a in-memory DB where we can record and query data
- TradingMetrics helps in calculation of metrics based on the stock and data available in the trading table.

### API flow

![plot](others/JPSample.drawio.png)
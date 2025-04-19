import yfinance as yf
import pandas as pd
from datetime import datetime

def fetch_stock_data(ticker, period="1d", interval="1m"):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period, interval=interval)
    return data

# Example usage
if __name__ == "__main__":
    data = fetch_stock_data("AAPL")
    print(data.head())
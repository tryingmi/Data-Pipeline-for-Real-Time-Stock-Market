# src/analyzer.py
import pandas as pd
import numpy as np
from data_fetcher import fetch_stock_data
from etl_pipeline import clean_data

def calculate_bollinger_bands(data, window=20, num_std=2):
    """
    Calculate Bollinger Bands for the given data
    Returns DataFrame with SMA, Upper Band, and Lower Band columns added
    """
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    if 'close' not in data.columns:
        raise ValueError("DataFrame must contain 'close' column")
    
    data['SMA'] = data['close'].rolling(window=window).mean()
    rolling_std = data['close'].rolling(window=window).std()
    data['Upper Band'] = data['SMA'] + (rolling_std * num_std)
    data['Lower Band'] = data['SMA'] - (rolling_std * num_std)
    return data

def calculate_rsi(data, window=14):
    """
    Calculate Relative Strength Index (RSI)
    Returns DataFrame with RSI column added
    """
    delta = data['close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))
    return data

if __name__ == "__main__":
    try:
        # Step 1: Fetch and clean data
        print("Fetching stock data...")
        raw_data = fetch_stock_data("AAPL", period="1mo", interval="1d")
        
        print("Cleaning data...")
        cleaned_data = clean_data(raw_data)
        
        # Step 2: Calculate technical indicators
        print("Calculating Bollinger Bands...")
        processed_data = calculate_bollinger_bands(cleaned_data)
        
        print("Calculating RSI...")
        processed_data = calculate_rsi(processed_data)
        
        # Display results
        print("\nProcessed Data with Technical Indicators:")
        print(processed_data[['close', 'SMA', 'Upper Band', 'Lower Band', 'RSI']].tail())
        
        # Save results
        processed_data.to_csv("data/AAPL_analyzed.csv")
        print("\nResults saved to data/AAPL_analyzed.csv")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Make sure you have:")
        print("1. Required packages installed (pandas, numpy, yfinance)")
        print("2. Internet connection for data fetching")
        print("3. data_fetcher.py and etl_pipeline.py in your src folder")
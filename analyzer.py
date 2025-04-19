import numpy as np
import pandas as pd

def calculate_bollinger_bands(data, window=20, num_std=2):
    data["SMA"] = data["close"].rolling(window=window).mean()
    data["Upper Band"] = data["SMA"] + (data["close"].rolling(window=window).std() * num_std)
    data["Lower Band"] = data["SMA"] - (data["close"].rolling(window=window).std() * num_std)
    return data

def calculate_rsi(data, window=14):
    delta = data["close"].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    data["RSI"] = 100 - (100 / (1 + rs))
    return data

# Example usage
if __name__ == "__main__":
    processed_data = calculate_bollinger_bands(processed_data)
    processed_data = calculate_rsi(processed_data)
    print(processed_data.tail())
# src/etl_pipeline.py
import pandas as pd
from data_fetcher import fetch_stock_data
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def clean_data(raw_data):
    """Clean and standardize stock data"""
    try:
        # Standardize column names
        raw_data.columns = raw_data.columns.str.lower()
        logger.info(f"Raw data columns: {raw_data.columns.tolist()}")
        
        # Select and rename columns for consistency
        column_map = {
            'open': 'open',
            'high': 'high',
            'low': 'low',
            'close': 'close',
            'volume': 'volume'
        }
        
        # Keep only columns that exist in the data
        available_cols = {k: v for k, v in column_map.items() 
                         if k in raw_data.columns}
        cleaned_data = raw_data[list(available_cols.keys())].rename(columns=available_cols)
        
        # Ensure datetime index
        if not isinstance(cleaned_data.index, pd.DatetimeIndex):
            cleaned_data.index = pd.to_datetime(cleaned_data.index)
            
        cleaned_data = cleaned_data.dropna()
        logger.info(f"Data cleaned successfully. Shape: {cleaned_data.shape}")
        return cleaned_data
        
    except Exception as e:
        logger.error(f"Error cleaning data: {str(e)}")
        raise

def calculate_technical_indicators(data, window=20):
    """Calculate technical indicators"""
    try:
        if 'close' not in data.columns:
            raise ValueError("Missing 'close' column for calculations")
            
        # Moving Averages
        data['SMA'] = data['close'].rolling(window=window).mean()
        data['EMA'] = data['close'].ewm(span=window, adjust=False).mean()
        
        # Daily Returns
        data['daily_return'] = data['close'].pct_change()
        
        logger.info("Technical indicators calculated successfully")
        return data
        
    except Exception as e:
        logger.error(f"Error calculating indicators: {str(e)}")
        raise

if __name__ == "__main__":
    try:
        # Fetch data
        logger.info("Fetching stock data...")
        raw_data = fetch_stock_data("AAPL", period="1d", interval="1m")
        
        # Clean data
        cleaned_data = clean_data(raw_data)
        
        # Calculate indicators
        processed_data = calculate_technical_indicators(cleaned_data)
        
        # Show results
        print("\nFirst 5 rows of processed data:")
        print(processed_data.head())
        
        print("\nLast 5 rows of processed data:")
        print(processed_data.tail())
        
    except Exception as e:
        logger.error(f"Pipeline failed: {str(e)}")
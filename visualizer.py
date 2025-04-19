# src/visualizer.py
import plotly.graph_objects as go
import pandas as pd
from data_fetcher import fetch_stock_data
from etl_pipeline import clean_data, calculate_technical_indicators

def plot_stock_data(data, ticker="AAPL"):
    """Create interactive visualization of stock data"""
    if not isinstance(data, pd.DataFrame) or data.empty:
        raise ValueError("Input data must be a non-empty pandas DataFrame")
    
    # Create figure
    fig = go.Figure()
    
    # Candlestick chart
    fig.add_trace(go.Candlestick(
        x=data.index,
        open=data['open'],
        high=data['high'],
        low=data['low'],
        close=data['close'],
        name='Price',
        increasing_line_color='green',
        decreasing_line_color='red'
    ))
    
    # Add technical indicators if available
    if 'SMA' in data.columns:
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data['SMA'],
            name='SMA (20)',
            line=dict(color='blue', width=1.5)
        ))
    
    if 'EMA' in data.columns:
        fig.add_trace(go.Scatter(
            x=data.index,
            y=data['EMA'],
            name='EMA (20)',
            line=dict(color='orange', width=1.5)
        ))
    
    # Update layout
    fig.update_layout(
        title=f'{ticker} Stock Analysis',
        xaxis_title='Date',
        yaxis_title='Price ($)',
        xaxis_rangeslider_visible=False,
        template='plotly_white'
    )
    
    fig.show()

if __name__ == "__main__":
    try:
        # Fetch and process data
        print("Fetching and processing data...")
        raw_data = fetch_stock_data("AAPL", period="1d", interval="1m")
        cleaned_data = clean_data(raw_data)
        processed_data = calculate_technical_indicators(cleaned_data)
        
        # Generate visualization
        print("Generating visualization...")
        plot_stock_data(processed_data, "AAPL")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Make sure you have:")
        print("- All required packages installed (pip install plotly pandas yfinance)")
        print("- Internet connection for data fetching")
        print("- Properly defined data_fetcher and etl_pipeline modules")
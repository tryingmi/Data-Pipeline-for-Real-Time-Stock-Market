from etl_pipeline import fetch_stock_data, clean_data, calculate_technical_indicators
from visualizer import plot_stock_data
import dash_app

if __name__ == "__main__":
    # ETL process
    data = fetch_stock_data("AAPL", period="1d", interval="1m")
    cleaned = clean_data(data)
    processed = calculate_technical_indicators(cleaned)
    
    # Visualize
    plot_stock_data(processed)
    
    # Start Dash app
    dash_app.app.run(host="0.0.0.0", port=8050)

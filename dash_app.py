import dash
from dash import dcc, html
import plotly.graph_objects as go

from data_fetcher import fetch_stock_data
from etl_pipeline import clean_data, calculate_technical_indicators
from visualizer import plot_stock_data

# Fetch and process data here
raw_data = fetch_stock_data("AAPL", period="1d", interval="1m")
cleaned_data = clean_data(raw_data)
processed_data = calculate_technical_indicators(cleaned_data)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(figure=plot_stock_data(processed_data)),
    dcc.Interval(id='interval-component', interval=60*1000, n_intervals=0)  # Auto-refresh
])

if __name__ == "__main__":
    dash_app.app.run(host="0.0.0.0", port=8050)



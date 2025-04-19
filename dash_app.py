import dash
from dash import dcc, html
import plotly.graph_objects as go
from src.visualizer import plot_stock_data

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(figure=plot_stock_data(processed_data)),
    dcc.Interval(id='interval-component', interval=60*1000, n_intervals=0)  # Auto-refresh
])

if __name__ == "__main__":
    app.run_server(debug=True)
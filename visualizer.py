import plotly.graph_objects as go

def plot_stock_data(data):
    fig = go.Figure()
    
    # Candlestick chart
    fig.add_trace(go.Candlestick(
        x=data.index,
        open=data['open'],
        high=data['high'],
        low=data['low'],
        close=data['close'],
        name='Price'
    ))
    
    # Moving Averages
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data['SMA'],
        name='SMA (20)',
        line=dict(color='blue')
    ))
    
    # Bollinger Bands
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data['Upper Band'],
        name='Upper Band',
        line=dict(color='red')
    ))
    fig.add_trace(go.Scatter(
        x=data.index,
        y=data['Lower Band'],
        name='Lower Band',
        line=dict(color='green')
    ))
    
    fig.update_layout(title="Stock Analysis Dashboard", xaxis_title="Date", yaxis_title="Price")
    fig.show()

# Example usage
if __name__ == "__main__":
    plot_stock_data(processed_data)
from etl_pipeline import fetch_stock_data, clean_data, calculate_technical_indicators

def test_pipeline():
    data = fetch_stock_data("AAPL", period="1d", interval="1m")
    assert not data.empty, "Fetched data is empty!"

    cleaned = clean_data(data)
    assert not cleaned.empty, "Cleaned data is empty!"

    processed = calculate_technical_indicators(cleaned)
    assert 'SMA' in processed.columns, "SMA column missing!"
    print("✅ Smoke test passed!")

if __name__ == "__main__":
    test_pipeline()

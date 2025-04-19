import sqlite3
import pandas as pd

def save_to_sqlite(data, db_name="stocks.db", table_name="stock_data"):
    conn = sqlite3.connect(db_name)
    data.to_sql(table_name, conn, if_exists="replace")
    conn.close()

def save_to_csv(data, filename="stock_data.csv"):
    data.to_csv(filename)

# Example usage
if __name__ == "__main__":
    save_to_sqlite(processed_data)
    save_to_csv(processed_data)
import yfinance as yf
import pandas as pd
from datetime import datetime

# Function to download intraday stock data and save it to an Excel file
def download_and_save_intraday_to_excel(stock_name, start_date, end_date):
    try:
        # Append ".NS" to the stock name if it doesn't already have it
        if not stock_name.endswith(".NS"):
            stock_name += ".NS"

        # Download intraday stock data using yfinance with a 1-minute timeframe
        data = yf.download(stock_name, start=start_date, end=end_date, interval='1m')

        # Convert datetime objects to timezone-unaware datetime objects
        data.index = data.index.tz_localize(None)

        # Create a DataFrame with the intraday data
        df = pd.DataFrame(data)

        # Save the data to an Excel file in the current directory
        excel_file_name = f'{stock_name}_intraday_{start_date}_{end_date}.xlsx'
        df.to_excel(excel_file_name)

        print(f"Intraday data saved to {excel_file_name}")
    except Exception as e:
        print(f'Error: {e}')

def main():
    stock_name = input("Enter the stock symbol (e.g., TATASTEEL): ")  # No need to specify ".NS"
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    download_and_save_intraday_to_excel(stock_name, start_date, end_date)

if __name__ == "__main__":
    main()

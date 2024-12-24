import yfinance as yf

def download_stock_data(ticker, start_date, end_date):
    """
    Download historical stock data and save to a CSV file.

    Parameters:
    ticker (str): The ticker symbol of the stock (e.g. 'ABI.BR').
    start_date (str): Start date in format 'YYYY-MM-DD'.
    end_date (str): End date in format 'YYYY-MM-DD'.
    output_file (str): Name of the CSV file to save.
    """
    print(f"downloading data for {ticker} from {start_date} to {end_date}...")
    try:
        from yahoo_fin import stock_info as si

        data = si.get_data(ticker, start_date, end_date)

        output_filename = f'{ticker}_data.csv'
        data.to_csv(output_filename, encoding='utf-8', decimal=',', sep=';')
        print(f'data saved in {output_filename}')
    except Exception as e:
        print(f"error during download: {e}")

def main():
    download_stock_data(
        # Colruyt = COLR.BR
        # Atos = ATO.PA
        ticker="COLR.BR",
        start_date="2023-01-01",
        end_date="2024-12-31"
    )

if __name__ == "__main__":
    print("Script executed as main program")
    main()

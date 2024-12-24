from yahooquery import Ticker
from datetime import datetime
import pandas as pd

def get_yahoo_finance_news(ticker, start_date, end_date):
    """
    Fetches news for a specific ticker from Yahoo Finance and filters by date range.
    Args:
        ticker (str): The ticker symbol (e.g., 'AAPL').
        start_date (str): The start date in 'YYYY-MM-DD' format.
        end_date (str): The end date in 'YYYY-MM-DD' format.
    Returns:
        pd.DataFrame: A DataFrame with the filtered news articles.
    """
    try:
        # Create a Ticker object for the given ticker symbol
        stock = Ticker(ticker)

        # Fetch the news articles for the ticker
        news = stock.news

        # List to store filtered news data
        news_data = []

        # Parse each article and filter by date
        for article in news:
            # Extract the article title and publication date
            title = article.get('title')
            date_str = article.get('date')
            date = datetime.utcfromtimestamp(date_str / 1000)  # Convert from milliseconds to datetime

            # Filter news based on the provided date range
            if start_date <= date.strftime('%Y-%m-%d') <= end_date:
                news_data.append({
                    'date': date,
                    'title': title
                })

        # Convert the filtered news data to a DataFrame
        news_df = pd.DataFrame(news_data)

        # If there are news articles, save them to a CSV file
        if not news_df.empty:
            filename = f"{ticker}_news_{start_date}_{end_date}.csv"
            news_df.to_csv(filename, index=False)
            print(f"News saved in {filename}")
        else:
            print("No news found for the specified period.")

    except Exception as e:
        print(f"Error fetching news for {ticker}: {e}")

def main():
    ticker = "AAPL"  
    start_date = "2024-01-01"
    end_date = "2024-12-31"
    get_yahoo_finance_news(ticker, start_date, end_date)

if __name__ == "__main__":
    print("Script executed as main program")
    main()
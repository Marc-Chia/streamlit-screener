from alpaca_trade_api.rest import REST

# Replace these with your Alpaca API keys
ALPACA_API_KEY = "AK95UUET1PLFPMQU551B"
ALPACA_SECRET_KEY = "joUq0nsy0YewxlLFxS6lctW400ynGKedase6NvUY"
BASE_URL = "https://paper-api.alpaca.markets"  # Use live API URL for a live account

# Initialize the Alpaca API
api = REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url=BASE_URL)

def fetch_real_time_data(tickers):
    stock_data = []

    for ticker in tickers:
        try:
            # Fetch the latest trade
            trade = api.get_latest_trade(ticker)

            # Fetch the latest quote
            quote = api.get_latest_quote(ticker)

            # Compile the data
            stock_data.append({
                "Ticker": ticker,
                "Price": trade.price,
                "Volume": trade.size,
                "Bid": quote.bid_price,
                "Ask": quote.ask_price,
            })

        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")

    return stock_data

# Test the function
if __name__ == "__main__":
    tickers = ["AAPL", "TSLA", "AMZN"]
    data = fetch_real_time_data(tickers)
    print(data)

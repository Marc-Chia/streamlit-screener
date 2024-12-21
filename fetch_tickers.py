from alpaca_trade_api.rest import REST

# Replace these with your Alpaca API keys
ALPACA_API_KEY = "AK95UUET1PLFPMQU551B"
ALPACA_SECRET_KEY = "joUq0nsy0YewxlLFxS6lctW400ynGKedase6NvUY"
BASE_URL = "https://paper-api.alpaca.markets"  # Use live API URL for a live account

# Initialize the Alpaca API
api = REST(ALPACA_API_KEY, ALPACA_SECRET_KEY, base_url=BASE_URL)

def fetch_small_cap_tickers():
    tickers = []
    try:
        # Fetch all active U.S. equity assets
        assets = api.list_assets(status="active", asset_class="us_equity")
        
        # Filter for small-cap stocks (e.g., market cap < $2B)
        for asset in assets:
            if asset.exchange in ["NYSE", "NASDAQ"]:  # Limit to major exchanges
                tickers.append(asset.symbol)
    except Exception as e:
        print(f"Error fetching tickers: {e}")
    return tickers

# Test the function
if __name__ == "__main__":
    tickers = fetch_small_cap_tickers()
    print(f"Fetched {len(tickers)} small-cap tickers.")
    print(tickers[:10])  # Show the first 10 tickers

from fetch_alpaca_data import fetch_real_time_data
from fetch_tickers import fetch_small_cap_tickers

def fetch_simulated_data():
    """
    Returns simulated stock data for testing when markets are closed.
    """
    return [
        {"Ticker": "AMC", "Price": 9.45, "Volume": 1200000, "AverageVolume": 500000, "Change %": 8.7},
        {"Ticker": "PLUG", "Price": 6.23, "Volume": 850000, "AverageVolume": 300000, "Change %": 10.5},
        {"Ticker": "NIO", "Price": 7.34, "Volume": 600000, "AverageVolume": 800000, "Change %": 4.2},
    ]

def ross_cameron_screener(use_simulated=False):
    """
    Filters stocks based on Ross Cameron's Small-Cap High Momentum criteria.
    Criteria:
      - Small Cap: Market cap ≤ $2B (handled during ticker selection)
      - Price: $1 ≤ Price ≤ $10
      - High Momentum: % Change > 5%
      - High Demand: Relative Volume (RVOL) > 2
      - Minimum Volume: > 100,000 shares
    """
    if use_simulated:
        data = fetch_simulated_data()
    else:
        # Fetch small-cap tickers dynamically
        tickers = fetch_small_cap_tickers()
        print(f"Fetched {len(tickers)} tickers.")
        
        # Fetch real-time data for the tickers
        data = fetch_real_time_data(tickers)

    # Apply filters
    momentum_stocks = []
    for stock in data:
        # Calculate RVOL
        rvol = stock["Volume"] / stock["AverageVolume"] if stock.get("AverageVolume", 0) > 0 else 0
        percent_change = stock["Change %"]

        # Filters
        if (
        stock["Price"] > 3 and stock["Price"] <= 30 and
        rvol > 4 and
        percent_change > 20 and
        stock["Volume"] > 500000 and
        stock.get("Float", 0) < 5000000 and  # Low Float
        stock.get("PreMarketChange", 0) > 10 and  # Pre-market Movers
        stock["Price"] >= stock.get("DayHigh", 0)  # New High of Day
        ):

            momentum_stocks.append({
                "Ticker": stock["Ticker"],
                "Price": stock["Price"],
                "Volume": stock["Volume"],
                "RVOL": round(rvol, 2),
                "% Change": round(percent_change, 2),
            })

    return momentum_stocks

if __name__ == "__main__":
    # Run the screener with simulated data when markets are closed
    results = ross_cameron_screener(use_simulated=True)
    print("Momentum Stocks:")
    for stock in results:
        print(stock)


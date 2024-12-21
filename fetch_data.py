import requests

def fetch_real_time_data(tickers):
    results = []
    for ticker in tickers[:20]:  # Limit to 20 tickers for testing
        url = f"https://api.polygon.io/v2/snapshot/locale/us/markets/stocks/tickers/{ticker}"
        params = {"apiKey": "MAdpLvQo8enywbnj_aWTedA826qmFDXp"}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json().get("ticker", {})
            if data:
                results.append({
                    "Ticker": ticker,
                    "Price": data["lastTrade"]["p"],
                    "Volume": data["day"]["v"],
                    "Change %": data["todaysChangePerc"]
                })
        else:
            print(f"Error fetching data for {ticker}: {response.status_code}")
    return results

# Test the function
if __name__ == "__main__":
    tickers = ["AMC", "GME", "PLUG"]  # Replace with dynamically fetched tickers
    stock_data = fetch_real_time_data(tickers)
    print(stock_data)


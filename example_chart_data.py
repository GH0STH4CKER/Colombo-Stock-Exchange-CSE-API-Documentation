import requests
import json
from datetime import datetime

# ==========================================
# CSE API: Historical Chart Data Fetcher
# ==========================================
# This script demonstrates how to fetch chart data, which requires a two-step process:
# 1. Fetch 'tradeSummary' to map a Symbol (e.g., LOLC.N0000) to an internal Stock ID.
# 2. Use the Stock ID to fetch the actual chart data.
#
# Output fields are documented below.
# ==========================================

# Base API URL
BASE_URL = "https://www.cse.lk/api/"

# ⚠️ CRITICAL: The API checks these headers. 
# Without 'Referer' and 'Origin', the API often returns an empty list [] or 403 errors.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Origin": "https://www.cse.lk",
    "Referer": "https://www.cse.lk/"
}

def get_stock_id(symbol):
    """
    Fetches the internal numeric ID for a given stock symbol.

    Args:
        symbol (str): The CSE stock symbol (e.g., "LOLC.N0000")

    Returns:
        int or None: Internal stock ID if found, else None
    """
    print(f"🔍 Searching for ID of symbol: {symbol}...")
    
    try:
        response = requests.post(BASE_URL + "tradeSummary", headers=HEADERS, data={})
        response.raise_for_status()
        
        all_stocks = response.json().get('reqTradeSummery', [])
        for stock in all_stocks:
            if stock['symbol'] == symbol:
                print(f"✅ Found ID: {stock['id']} for {symbol}")
                return stock['id']
        
        print(f"❌ Symbol {symbol} not found in trade summary.")
        return None

    except Exception as e:
        print(f"❌ Error fetching stock map: {e}")
        return None

def get_chart_data(stock_id, period="5"):
    """
    Fetches historical price data using the numeric Stock ID.

    Args:
        stock_id (int): Internal CSE stock ID
        period (str): Period code
            "1" = Intraday (today, ~1-minute intervals)
            "2" = 1 Week
            "3" = 1 Month
            "4" = 3 Months
            "5" = 1 Year (daily history – best for standard analysis)

    Returns:
        list of dict or None: List of OHLC data points
    """
    print(f"📉 Fetching chart data for stock ID {stock_id} (period={period})...")

    payload = {
        "stockId": str(stock_id),
        "period": period
    }
    
    try:
        response = requests.post(BASE_URL + "companyChartDataByStock", headers=HEADERS, data=payload)
        response.raise_for_status()
        
        result = response.json()
        if 'chartData' in result and result['chartData']:
            points = result['chartData']
            print(f"🎉 Retrieved {len(points)} data points.")
            return points
        else:
            print("⚠️ Request successful but no chart data found.")
            return None

    except Exception as e:
        print(f"❌ Error fetching chart: {e}")
        return None

def explain_point_fields():
    """
    Prints documentation for each field found in a chart data point.
    """
    print("""
📌 Chart Data Field Definitions:
  t   (int): Timestamp in milliseconds (Epoch). Convert with datetime.fromtimestamp(t/1000).
  o   (float or null): Opening price during this period (null if not reported).
  h   (float): Highest traded price in this period.
  l   (float): Lowest traded price in this period.
  p   (float): Closing or representative price for this period.
  q   (int): Volume – number of shares traded.
  s   (float): Total turnover value (volume × price).
  c   (float or null): Price change vs. previous close (null if not provided).
  pc  (float or null): Previous close price (null if not provided).
  n   (int or null): Number of trades in the period (if available).
  id  (int): Internal chart record ID.
""")

def display_point(point, label):
    """
    Prints a human-friendly single data point.
    """
    ts = point.get('t')
    readable = datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M:%S') if ts else "N/A"
    print(f"[{label}] {readable} | O: {point.get('o')} H: {point.get('h')} L: {point.get('l')} P: {point.get('p')} | Vol: {point.get('q')}")

# ----------------------
# Main Execution
# ----------------------
if __name__ == "__main__":
    # Show field docs
    explain_point_fields()

    # Example symbol - LOLC Holdings
    symbol = "LOLC.N0000"
    stock_id = get_stock_id(symbol)

    if stock_id:
        chart_data = get_chart_data(stock_id, period="5")

        if chart_data:
            print("\n--- Sample Output ---")
            display_point(chart_data[0], "Oldest")
            display_point(chart_data[-1], "Newest")

            # Optional: Save all data
            with open("market_data.json", "w") as f:
                json.dump(chart_data, f, indent=4)
            print(f"\n✅ All {len(chart_data)} records saved to market_data.json")

import requests
from datetime import datetime, timedelta

# ===== ENTER YOUR CREDENTIALS HERE =====
CHANNEL_ID = "2894396"                # From your channel URL
READ_API_KEY = "EGKZKTZNQKK86VXZ"     # From API Keys tab
# =======================================

def fetch_historical_data():
    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json"
    params = {
        "api_key": READ_API_KEY,
        "results": 10  # Get last 10 records regardless of time
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        print(f"DEBUG: API Response - {response.status_code}")  # Debug line
        if response.status_code == 200:
            data = response.json()
            print(f"DEBUG: Raw API Response - {data}")  # Debug line
            return data.get('feeds', [])
        return None
    except Exception as e:
        print(f"Connection Error: {str(e)}")
        return None

def display_data(feeds):
    if not feeds:
        print("\nCRITICAL: No data found. Immediate checks needed:")
        print("1. Is virtual_station.py running and showing 'HTTP 200'?")
        print("2. Verify READ_API_KEY matches your channel's Read Key")
        print("3. Manually check: https://thingspeak.com/channels/2894396")
        print("4. Try this direct link:")
        print(f"   https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=2")
        return
    
    print(f"\nSUCCESS: Found {len(feeds)} data points")
    for feed in feeds:
        print(f"\nTimestamp: {feed.get('created_at')}")
        print(f"Temperature: {feed.get('field1')}°C")
        print(f"Humidity: {feed.get('field2')}%")
        print(f"CO2: {feed.get('field3')}ppm")

if __name__ == "__main__":
    print("Fetching historical data from ThingSpeak...")
    data = fetch_historical_data()
    display_data(data)
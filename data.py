import requests
from config import BASE_URL


def get_klines(symbol, interval, limit=200):
    """
    دریافت کندل‌های بازار از Binance
    """

    url = f"{BASE_URL}/api/v3/klines"

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

    return None

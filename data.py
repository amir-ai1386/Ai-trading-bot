import requests
from config import BASE_URL

session = requests.Session()


def get_klines(symbol, interval, limit=200):
    """
    دریافت کندل‌های بازار از Binance
    """

    url = f"{BASE_URL}/api/v3/klines"

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit,
    }

    try:

        response = session.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:

        print(f"Binance Error ({symbol}-{interval}) : {e}")

        return None

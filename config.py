import os

# Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Binance
BASE_URL = "https://api.binance.com"

# Symbols
SYMBOLS = [
    "BTCUSDT",
    "ETHUSDT",
    "XRPUSDT",
    "SOLUSDT"
]

# Timeframes
TIMEFRAMES = [
    "15m",
    "1h",
    "4h"
]

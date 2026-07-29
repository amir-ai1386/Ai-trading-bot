import pandas as pd
from ta.trend import EMAIndicator
from ta.momentum import RSIIndicator


def analyze_market(klines):

    if len(klines) < 60:
        return "NO TRADE"

    df = pd.DataFrame(klines)

    df["close"] = df[4].astype(float)
    df["volume"] = df[5].astype(float)

    df["ema20"] = EMAIndicator(df["close"], window=20).ema_indicator()
    df["ema50"] = EMAIndicator(df["close"], window=50).ema_indicator()

    df["rsi"] = RSIIndicator(df["close"], window=14).rsi()

    last = df.iloc[-1]

    avg_volume = df["volume"].tail(20).mean()

    # LONG
    if (
        last["ema20"] > last["ema50"]
        and last["rsi"] > 50
        and last["rsi"] < 70
        and last["volume"] > avg_volume
        and last["close"] > last["ema20"]
    ):
        return "LONG"

    # SHORT
    if (
        last["ema20"] < last["ema50"]
        and last["rsi"] < 50
        and last["rsi"] > 30
        and last["volume"] > avg_volume
        and last["close"] < last["ema20"]
    ):
        return "SHORT"

    return "NO TRADE"

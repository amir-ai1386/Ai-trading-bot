def analyze_market(klines):
    """
    تحلیل اولیه بازار
    """

    if not klines:
        return None

    last_close = float(klines[-1][4])
    previous_close = float(klines[-2][4])

    if last_close > previous_close:
        return "LONG"

    elif last_close < previous_close:
        return "SHORT"

    else:
        return "NO TRADE"

from config import SYMBOLS, TIMEFRAMES
from data import get_klines
from strategy import analyze_market
from notifier import send_message
from database import create_tables, save_trade


def run():

    create_tables()

    for symbol in SYMBOLS:

        for timeframe in TIMEFRAMES:

            try:

                klines = get_klines(symbol, timeframe)

                signal = analyze_market(klines)

                if signal == "NO TRADE":
                    continue

                message = (
                    f"📊 {symbol}\n"
                    f"⏰ Timeframe: {timeframe}\n"
                    f"📈 Signal: {signal}"
                )

                save_trade(
                    symbol=symbol,
                    timeframe=timeframe,
                    signal=signal
                )

                print(message)

                send_message(message)

            except Exception as e:
                print(f"{symbol} {timeframe} -> {e}")


if __name__ == "__main__":
    run()

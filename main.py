from config import SYMBOLS, TIMEFRAMES
from data import get_klines
from strategy import analyze_market
from notifier import send_message


def run():

    for symbol in SYMBOLS:

        for timeframe in TIMEFRAMES:

            klines = get_klines(symbol, timeframe)

            signal = analyze_market(klines)

            message = (
                f"📊 {symbol}\n"
                f"⏰ Timeframe: {timeframe}\n"
                f"📈 Signal: {signal}"
            )

            print(message)

            # ارسال به تلگرام
            # send_message(message)


if __name__ == "__main__":
    run()

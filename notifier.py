import requests
from config import BOT_TOKEN, CHAT_ID

session = requests.Session()


def send_message(message):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    try:

        response = session.post(
            url,
            data=payload,
            timeout=10
        )

        response.raise_for_status()

        return True

    except requests.exceptions.RequestException as e:

        print(f"Telegram Error: {e}")

        return False

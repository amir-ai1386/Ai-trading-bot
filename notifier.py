import requests
from config import BOT_TOKEN, CHAT_ID


def send_message(message):
    """
    ارسال پیام به تلگرام
    """

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    data = {
        "chat_id": CHAT_ID,
        "text": message
    }

    response = requests.post(url, data=data)

    return response.json()

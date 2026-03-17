import os
import requests


MAX_MESSAGE_LENGTH = 2000


def split_message(message):
    return [message[i:i+MAX_MESSAGE_LENGTH] for i in range(0, len(message), MAX_MESSAGE_LENGTH)]


def send_to_discord(message: str):

    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    if not webhook_url:
        print("Missing DISCORD_WEBHOOK_URL")
        return

    messages = split_message(message)

    for part in messages:

        data = {
            "content": part
        }

        response = requests.post(webhook_url, json=data)

        if response.status_code != 204:
            print(f"Failed to send message: {response.status_code}")
            print(response.text)
            return

    print("Message sent successfully")

import os
import requests


def send_to_discord(message: str):

    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    if not webhook_url:
        print("Missing DISCORD_WEBHOOK_URL")
        return

    data = {
        "content": message
    }

    response = requests.post(webhook_url, json=data)

    if response.status_code == 204:
        print("Message sent successfully")
    else:
        print(f"Failed to send message: {response.status_code}")
        print(response.text)

import os
import requests

MAX_MESSAGE_LENGTH = 2000


def split_message(message, max_length=MAX_MESSAGE_LENGTH):
    parts = []

    while len(message) > max_length:

        chunk = message[:max_length]

        # 1️⃣ Essaye de couper à un saut de ligne
        split_index = chunk.rfind("\n")

        # 2️⃣ Sinon coupe à un espace
        if split_index == -1:
            split_index = chunk.rfind(" ")

        # 3️⃣ Si rien trouvé, coupe brutalement
        if split_index == -1:
            split_index = max_length

        parts.append(message[:split_index].strip())

        message = message[split_index:].strip()

    if message:
        parts.append(message)

    return parts


def send_to_discord(message: str):

    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")

    if not webhook_url:
        print("Missing DISCORD_WEBHOOK_URL")
        return

    messages = split_message(message)

    for i, part in enumerate(messages):

        data = {
            "content": f"({i+1}/{len(messages)})\n\n{part}"
        }

        response = requests.post(webhook_url, json=data)

        if response.status_code != 204:
            print(f"Failed to send message: {response.status_code}")
            print(response.text)
            return

    print("Message sent successfully")

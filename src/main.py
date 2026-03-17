from src.discord_sender import send_to_discord


def main():

    message = "🚀 SITREP Bot is now operational."

    send_to_discord(message)


if __name__ == "__main__":
    main()

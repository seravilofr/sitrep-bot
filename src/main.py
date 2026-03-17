from news_fetcher import fetch_articles
from discord_sender import send_to_discord


def main():

    articles = fetch_articles()

    if not articles:
        send_to_discord("⚠️ No articles found.")
        return

    message = f"📰 Retrieved {len(articles)} articles."

    send_to_discord(message)


if __name__ == "__main__":
    main()

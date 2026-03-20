from news_fetcher import fetch_articles
from brief_generator import generate_brief
from discord_sender import send_to_discord
from config_loader import load_config

def main():
    config = load_config()
    articles = fetch_articles(config)
    if not articles:
        send_to_discord("⚠️ No articles found.")
        return
    brief = generate_brief(articles, config)
    if not brief:
        send_to_discord("⚠️ Failed to generate brief.")
        return
    send_to_discord(brief)

if __name__ == "__main__":
    main()

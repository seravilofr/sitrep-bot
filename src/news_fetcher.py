import os
import requests
from config_loader import load_config


def fetch_articles():

    config = load_config()
    blocked_sources = [s.lower() for s in config.get("blocked_sources", [])]

    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        print("Missing NEWS_API_KEY")
        return []

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": "geopolitics OR war OR military OR conflict OR diplomacy",
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": config.get("articles_to_scan", 40),
        "apiKey": api_key
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error fetching news:", response.status_code)
        print(response.text)
        return []

    data = response.json()

    articles = []

    for article in data.get("articles", []):

        source_name = article.get("source", {}).get("name") or ""
        source_name_clean = source_name.strip().lower()

        # 🔥 filtre blacklist
        if any(blocked in source_name_clean for blocked in blocked_sources):
            print(f"Filtered source: {source_name}")
            continue

        articles.append({
            "title": article.get("title"),
            "description": article.get("description"),
            "url": article.get("url"),
            "source": source_name
        })

    return articles

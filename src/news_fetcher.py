import os
import requests


def fetch_articles():

    api_key = os.getenv("NEWS_API_KEY")

    if not api_key:
        print("Missing NEWS_API_KEY")
        return []

    url = "https://newsapi.org/v2/everything"

    params = {
        "q": "geopolitics OR war OR military OR conflict OR diplomacy",
        "language": "en",
        "sortBy": "publishedAt",
        "pageSize": 40,
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
        articles.append({
            "title": article.get("title"),
            "description": article.get("description"),
            "url": article.get("url"),
            "source": article.get("source", {}).get("name")
        })

    return articles

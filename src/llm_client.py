import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_sitrep(articles, config):

    articles_text = ""

    for i, article in enumerate(articles):
        articles_text += f"""
Article {i+1}:
Title: {article['title']}
Description: {article['description']}
Source: {article['source']}
URL: {article['url']}

"""

    prompt = f"""
You are a geopolitical intelligence analyst.

Your task is to:

1. Group articles by geopolitical event (avoid duplicates)
2. Identify the {config['events_per_brief']} most important events
3. Summarize each event in {config['sentences_per_event']} sentences
4. Provide a "Strategic Trend"
5. Provide a "Global Risk Level" (score from 1 to 10 + label)

Rules:
- Focus only on geopolitics, war, diplomacy, international tensions
- Ignore domestic politics unless geopolitically relevant
- No speculation
- Neutral analytical tone
- Use multiple sources when relevant

Articles:
{articles_text}

Output format:

🌍 SITREP – [DATE]

1️⃣ [Event title]
[Summary]

Sources:
- [Source]

...

📈 Strategic Trend
[Text]

⚠ Global Risk Level
[X/10 — Label]
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content

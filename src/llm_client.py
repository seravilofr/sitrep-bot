import os
from openai import OpenAI
from datetime import datetime

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

    today = datetime.now().strftime("%B %d, %Y")

    prompt = f"""
You are a geopolitical intelligence analyst producing a daily SITREP.

Your task is to:

1. Group articles by geopolitical event and underlying situation

2. Avoid duplicate coverage of the same exact development

3. However, if a major geopolitical situation has multiple distinct strategic dimensions, you may create separate entries.

Examples of valid separate entries for the same situation:
- Military developments (e.g. strikes, battles)
- Economic consequences (e.g. trade disruption, sanctions, energy markets)
- Strategic chokepoints (e.g. Strait of Hormuz, shipping lanes)
- Diplomatic or political escalation

4. Each entry must represent a distinct strategic angle, not a repetition of the same information

5. Identify the {config['events_per_brief']} most important events, ensuring diversity across regions and topics

6. Avoid over-representing a single conflict unless it is overwhelmingly dominant in global news

7. Each event should ideally reflect a different region, actor, or strategic issue

8. Summarize each event in {config['sentences_per_event']} sentences

9. Provide a "Strategic Trend"

10. Provide a "Global Risk Level" (score from 1 to 10 + label)

Rules:
- Focus only on geopolitics, war, diplomacy, international tensions
- Ignore domestic politics unless geopolitically relevant
- No speculation
- Neutral analytical tone (CIA-style briefing)
- Use multiple sources when relevant
- Do not repeat the same event with slightly different wording
- It is allowed to cover the same conflict multiple times ONLY if each entry provides a clearly different strategic perspective
- Prioritize diversity of insights over redundancy

Articles:
{articles_text}

Output format:

🌍 SITREP – {today}

1️⃣ [Event title]
[2-3 sentence summary]

Sources:
- [Source name]

2️⃣ [Event title]
[Summary]

Sources:
- [Source name]

...

📈 Strategic Trend
[Concise strategic insight synthesizing multiple events]

⚠ Global Risk Level
[X/10 — Low / Medium / High]
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content

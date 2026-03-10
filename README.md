# SITREP Bot

![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)

**SITREP** stands for **Situation Report**, a standard military intelligence briefing format used to summarize key developments in a concise and structured way.

## Overview

**SITREP Bot** is an automated geopolitical briefing agent that publishes a daily intelligence-style situation report to a Discord channel.

Every morning, the bot analyzes recent global news from reliable international media sources and produces a concise briefing highlighting the most strategically significant geopolitical developments from the past 24 hours.

The output is designed to resemble a **neutral intelligence briefing**, focusing on strategic implications rather than speculation or commentary.

At the end of each briefing, the bot also includes a **historical geopolitical event that occurred on the same day in history**, providing additional context and perspective.

The project is lightweight, configurable, and intended to run automatically with minimal cost.

---

# Features

- Daily automated geopolitical briefing
- Coverage of global geopolitical events from the past 24 hours
- AI-based selection of the most strategically important developments
- Concise intelligence-style summaries
- Strategic trend analysis
- Global risk level assessment
- **“This Day in Geopolitical History” historical event**
- Configurable parameters (number of events, summary length, etc.)
- Discord integration
- On-demand briefing command
- Open-source and lightweight

---

# Example Output

```
🌍 SITREP – March 12, 2026

1️⃣ Ukraine
Russian forces intensified artillery activity near Kupiansk while Ukrainian forces conducted counter-battery strikes. The escalation suggests continued pressure on northeastern Ukrainian defensive lines.

Source: Reuters  
https://www.reuters.com/...

2️⃣ Middle East
US naval forces intercepted drones launched from Houthi-controlled territory toward shipping lanes in the Red Sea. The attacks continue to threaten maritime trade routes.

Source: BBC  
https://www.bbc.com/...

3️⃣ China / Taiwan
Chinese military aircraft entered Taiwan’s air defense identification zone during new PLA exercises near the island. The maneuvers appear designed to increase pressure ahead of diplomatic engagements.

Source: Financial Times  
https://...

📈 Strategic Trend  
Maritime security tensions are increasing across several regions, particularly in the Red Sea and the Western Pacific.

⚠ Global Risk Level  
6 / 10 — Medium

📜 This Day in Geopolitical History  
1947 — The Truman Doctrine was announced by U.S. President Harry S. Truman, marking the beginning of a major shift in American foreign policy and the early stages of the Cold War containment strategy.
```

---

# Topics Covered

The bot prioritizes news related to:

- geopolitics
- international relations
- military activity
- war and armed conflicts
- diplomatic developments
- international tensions
- strategic alliances and sanctions

### Excluded topics

The bot ignores:

- domestic politics
- crime and local incidents
- sports
- entertainment
- economic news unrelated to geopolitics

Domestic political events may still be included when they have **clear geopolitical implications** (e.g. coups, civil wars, independence conflicts).

---

# Configuration

The bot behavior is controlled through a configuration file.

Example `config.yaml`:

```yaml
events_per_brief: 5
sentences_per_event: 3
articles_to_scan: 40
article_time_window_hours: 24
timezone: Europe/Paris
briefing_time: "08:00"
risk_scale: "1-10"
allow_duplicate_events: false
```

This allows the user to easily adjust parameters such as:

- number of events per briefing
- summary length
- number of articles analyzed
- briefing time

No code modification is required.

---

# How It Works

The bot follows these steps:

1. Retrieve 30–50 recent articles from trusted international media sources.
2. Filter articles for geopolitical relevance.
3. Send the collected articles to an AI model.
4. The AI groups articles by event and identifies the most strategically significant developments.
5. Generate concise intelligence-style summaries.
6. Produce a strategic trend analysis and global risk score.
7. Retrieve a **historical geopolitical event that occurred on the same calendar day**.
8. Publish the complete briefing to Discord.

---

# Running the Bot

The bot runs automatically every day at:

```
08:00 Europe/Paris
```

It can also be triggered manually with a Discord command:

```
/brief
```

---

# Requirements

- Python 3.10+
- Discord webhook or bot token
- News data source API
- AI model API access

Dependencies are listed in:

```
requirements.txt
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/sitrep-bot.git
cd sitrep-bot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your API keys:

```
OPENAI_API_KEY=your_api_key
NEWS_API_KEY=your_api_key
DISCORD_WEBHOOK_URL=your_webhook
```

---

# Configuration File

SITREP Bot behavior can be customized through the `config.yaml` file.

Example:

```yaml
events_per_brief: 5
sentences_per_event: 3
articles_to_scan: 40
article_time_window_hours: 24
timezone: Europe/Paris
briefing_time: "08:00"
risk_scale: "1-10"
allow_duplicate_events: false
```

Adjust these values to change how the daily briefing is generated.

---

# Contributing

Contributions are welcome.

If you want to improve the project:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

Please keep changes focused and well documented.

---

# Project Goals

SITREP Bot aims to demonstrate how AI agents can automate the synthesis of complex geopolitical information into concise daily intelligence briefings.

The project focuses on:

- clarity
- reproducibility
- configurability
- minimal operational cost

---

# License

This project is licensed under the **GNU General Public License v3.0 (GPL-3.0)**.

You are free to use, modify, and distribute this software under the terms of the GPL-3.0 license. Any derivative work must also be distributed under the same license.

See the `LICENSE` file for details.

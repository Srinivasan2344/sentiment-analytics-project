import os
import json
from pathlib import Path

from dotenv import load_dotenv
from newsapi import NewsApiClient
from kafka import KafkaProducer

# Load .env
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

API_KEY = os.getenv("NEWS_API_KEY")

newsapi = NewsApiClient(api_key=API_KEY)

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

response = newsapi.get_everything(
    q="stock market OR finance OR Tesla OR Apple OR Microsoft",
    language="en",
    sort_by="publishedAt",
    page_size=5
)

articles = response["articles"]

print(f"Fetched {len(articles)} articles")

for article in articles:

    news = {
        "title": article["title"] or "No Title",
        "content": article["description"] or "",
        "source": article["source"]["name"],
        "url": article["url"],
        "company": "Unknown",
        "published_at": article["publishedAt"]
    }

    producer.send("financial-news", news)

    print(f"Sent: {news['title']}")

producer.flush()

print("All News Sent Successfully")
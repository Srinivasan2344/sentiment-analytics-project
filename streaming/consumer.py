import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, PROJECT_ROOT)


from kafka import KafkaConsumer
import json
from datetime import datetime

from services.sentiment import analyze_sentiment
from database.connection import SessionLocal
from database.crud import save_news, save_sentiment

consumer = KafkaConsumer(
    "financial-news",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    group_id="financial-news-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Listening for financial news...")

db = SessionLocal()

for message in consumer:
    try:
        news = message.value

        print("Received:", news)

        saved_news = save_news(
            db=db,
            title=news["title"],
            content=news["content"],
            source=news["source"],
            url=news["url"],
            company=news["company"],
            published_at=datetime.fromisoformat(news["published_at"])
        )

        result = analyze_sentiment(news["content"])

        save_sentiment(
            db=db,
            news_id=saved_news.id,
            sentiment=result["sentiment"],
            score=result["confidence"],
            confidence=result["confidence"]
        )

        print("Saved Successfully")
        print(result)

    except Exception as e:
        print("Error:", e)
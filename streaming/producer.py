from kafka import KafkaProducer
import json
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

news = {
    "title": "Tesla Q2 Earnings",
    "content": "Tesla shares surged after reporting strong quarterly earnings.",
    "source": "Reuters",
    "url": f"https://example.com/news/{datetime.now().timestamp()}",
    "company": "Tesla",
    "published_at": datetime.now().isoformat()
}

producer.send("financial-news", news)
producer.flush()

print("News Sent Successfully")
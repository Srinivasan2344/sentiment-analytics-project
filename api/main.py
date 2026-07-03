from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database.connection import get_db
from database.crud import (
    get_all_news,
    get_news_by_id,
    get_all_sentiments
)

app = FastAPI(title="AI-Powered Financial News & Sentiment Analysis Engine")


@app.get("/")
def home():
    return {
        "message": "Financial News Sentiment Analysis API Running"
    }


@app.get("/news")
def fetch_news(db: Session = Depends(get_db)):
    return get_all_news(db)


@app.get("/news/{news_id}")
def fetch_news_by_id(news_id: int, db: Session = Depends(get_db)):
    news = get_news_by_id(db, news_id)

    if news is None:
        raise HTTPException(status_code=404, detail="News Not Found")

    return news


@app.get("/sentiment")
def fetch_sentiments(db: Session = Depends(get_db)):
    return get_all_sentiments(db)
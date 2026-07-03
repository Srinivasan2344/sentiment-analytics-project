from database.models import News, Sentiment

def save_news(db, title, content, source, url, company, published_at):
    news = News(
        title=title,
        content=content,
        source=source,
        url=url,
        company=company,
        published_at=published_at
    )
    db.add(news)
    db.commit()
    db.refresh(news)
    return news


def save_sentiment(db, news_id, sentiment, score, confidence):
    sentiment_record = Sentiment(
        news_id=news_id,
        sentiment=sentiment,
        score=score,
        confidence=confidence
    )
    db.add(sentiment_record)
    db.commit()
    db.refresh(sentiment_record)
    return sentiment_record


from database.models import News, Sentiment


def get_all_news(db):
    return db.query(News).all()


def get_news_by_id(db, news_id: int):
    return db.query(News).filter(News.id == news_id).first()


def get_all_sentiments(db):
    return db.query(Sentiment).all()
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from database.connection import Base


class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(500), nullable=False)
    content = Column(Text, nullable=False)
    source = Column(String(255), nullable=False)
    url = Column(String(1000), unique=True, nullable=False)
    company = Column(String(100), nullable=True)
    published_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Sentiment(Base):
    __tablename__ = "sentiment"

    id = Column(Integer, primary_key=True, index=True)
    news_id = Column(Integer, ForeignKey("news.id"), nullable=False)
    sentiment = Column(String(20), nullable=False)
    score = Column(Float, nullable=False)
    confidence = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class MarketPrediction(Base):
    __tablename__ = "market_prediction"

    id = Column(Integer, primary_key=True, index=True)
    stock = Column(String(20), nullable=False)
    prediction = Column(String(20), nullable=False)
    impact_score = Column(Float, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


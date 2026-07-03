from sqlalchemy import create_engine
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)


def get_news():
    query = "SELECT * FROM news ORDER BY created_at DESC"
    return pd.read_sql(query, engine)


def get_sentiment():
    query = "SELECT * FROM sentiment ORDER BY created_at DESC"
    return pd.read_sql(query, engine)


def get_prediction():
    query = "SELECT * FROM market_prediction ORDER BY created_at DESC"
    return pd.read_sql(query, engine)
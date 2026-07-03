# AI-Powered Financial News & Sentiment Analysis Engine

## Overview

The AI-Powered Financial News & Sentiment Analysis Engine is a real-time financial news analysis system that collects financial news, streams it through Apache Kafka, performs AI-based sentiment analysis using Hugging Face Transformers, stores the processed data in PostgreSQL, and exposes REST APIs using FastAPI. A Streamlit dashboard provides an interactive visualization of the analyzed data.

---

# Features

* Real-time Financial News Collection
* Apache Kafka Streaming
* AI-based Sentiment Analysis
* PostgreSQL Database Storage
* REST API using FastAPI
* Interactive Streamlit Dashboard
* Dockerized Deployment
* Company-wise News Search
* Sentiment Visualization
* Confidence Score Analysis

---

# Tech Stack

| Technology                | Purpose                   |
| ------------------------- | ------------------------- |
| Python                    | Backend Development       |
| FastAPI                   | REST API                  |
| PostgreSQL                | Database                  |
| SQLAlchemy                | ORM                       |
| Apache Kafka              | Message Streaming         |
| Hugging Face Transformers | Sentiment Analysis        |
| Streamlit                 | Dashboard                 |
| Docker                    | Containerization          |
| NewsAPI                   | Financial News Collection |

---

# Project Structure

```
AI-Powered Financial News & Sentiment Analysis Engine
│
├── api/
│   └── main.py
│
├── dashboard/
│   └── app.py
│
├── database/
│   ├── connection.py
│   ├── models.py
│   ├── crud.py
│   └── init.py
│
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
│
├── news/
│   └── fetch_news.py
│
├── services/
│   └── sentiment.py
│
├── streaming/
│   ├── producer.py
│   └── consumer.py
│
├── requirements.txt
├── .env
└── README.md
```

---

# System Architecture

```
                NewsAPI

                   │

                   ▼

         Financial News Fetcher

                   │

                   ▼

           Kafka Producer

                   │

                   ▼

             Apache Kafka

                   │

                   ▼

           Kafka Consumer

                   │

                   ▼

      Hugging Face Sentiment Model

                   │

                   ▼

             PostgreSQL

           ▲              ▲

           │              │

        FastAPI       Streamlit

           │

           ▼

         End Users
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/AI-Powered-Financial-News-Sentiment-Analysis-Engine.git

cd AI-Powered-Financial-News-Sentiment-Analysis-Engine
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file.

```
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/financial_sentiment_db

NEWS_API_KEY=YOUR_NEWS_API_KEY
```

---

# Database Initialization

```bash
python -m database.init
```

---

# Start Kafka Producer

```bash
python streaming/producer.py
```

---

# Start Kafka Consumer

```bash
python streaming/consumer.py
```

---

# Run FastAPI

```bash
uvicorn api.main:app --reload
```

API Documentation

```
http://localhost:8000/docs
```

---

# Run Streamlit Dashboard

```bash
streamlit run dashboard/app.py
```

Dashboard URL

```
http://localhost:8501
```

---

# Docker Deployment

Build Containers

```bash
docker compose -f docker/docker-compose.yml up --build
```

Stop Containers

```bash
docker compose -f docker/docker-compose.yml down
```

---

# API Endpoints

### Get All News

```
GET /news
```

### Get All Sentiment Records

```
GET /sentiment
```

### Get Market Predictions

```
GET /prediction
```

---

# Workflow

1. Fetch financial news from NewsAPI.
2. Publish news messages to Apache Kafka.
3. Kafka Consumer reads incoming news.
4. AI model predicts sentiment.
5. Store results in PostgreSQL.
6. FastAPI exposes REST endpoints.
7. Streamlit dashboard visualizes the data.

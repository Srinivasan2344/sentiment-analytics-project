import streamlit as st
import pandas as pd
from database import get_news, get_sentiment, get_prediction
from charts import sentiment_pie, company_chart, trend_chart
from streamlit_autorefresh import st_autorefresh

# -------------------- PAGE CONFIG -------------------- #

st.set_page_config(
    page_title="AI Financial News Dashboard",
    page_icon="📈",
    layout="wide"
)

# Auto Refresh every 30 seconds
st_autorefresh(interval=30000, key="dashboard_refresh")

st.title("📈 AI Financial News & Sentiment Dashboard")
st.markdown("---")

# -------------------- LOAD DATA -------------------- #

news = get_news()
sentiment = get_sentiment()

try:
    prediction = get_prediction()
except:
    prediction = pd.DataFrame()

# -------------------- SIDEBAR -------------------- #

st.sidebar.header("Filters")

if not news.empty and "company" in news.columns:

    companies = sorted(news["company"].fillna("Unknown").unique())

    selected_company = st.sidebar.selectbox(
        "Company",
        ["All"] + companies,
        key="company_filter"
    )

    if selected_company != "All":
        news = news[
            news["company"] == selected_company
        ]

# -------------------- SEARCH -------------------- #

search = st.text_input(
    "🔍 Search News",
    key="search_box"
)

if search and "title" in news.columns:
    news = news[
        news["title"]
        .fillna("")
        .str.contains(search, case=False)
    ]

# -------------------- METRICS -------------------- #

total_news = len(news)

positive = 0
negative = 0
neutral = 0

if not sentiment.empty:

    positive = len(
        sentiment[
            sentiment["sentiment"] == "positive"
        ]
    )

    negative = len(
        sentiment[
            sentiment["sentiment"] == "negative"
        ]
    )

    neutral = len(
        sentiment[
            sentiment["sentiment"] == "neutral"
        ]
    )

c1, c2, c3, c4 = st.columns(4)

c1.metric("📰 Total News", total_news)
c2.metric("😊 Positive", positive)
c3.metric("😐 Neutral", neutral)
c4.metric("☹️ Negative", negative)

st.markdown("---")

# -------------------- CHARTS -------------------- #

st.subheader("📊 Analytics")

col1, col2 = st.columns(2)

with col1:

    st.plotly_chart(
        sentiment_pie(sentiment),
        use_container_width=True,
        key="pie_chart"
    )

with col2:

    st.plotly_chart(
        company_chart(news),
        use_container_width=True,
        key="company_chart"
    )

st.plotly_chart(
    trend_chart(news),
    use_container_width=True,
    key="trend_chart"
)

st.markdown("---")

# -------------------- NEWS -------------------- #

st.subheader("📰 Latest News")

if not news.empty:

    columns = []

    for col in [
        "title",
        "company",
        "source",
        "published_at"
    ]:
        if col in news.columns:
            columns.append(col)

    st.dataframe(
        news[columns],
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning("No News Available")

st.markdown("---")

# -------------------- SENTIMENT -------------------- #

st.subheader("😊 Sentiment Results")

if not sentiment.empty:

    columns = []

    for col in [
        "news_id",
        "sentiment",
        "confidence"
    ]:
        if col in sentiment.columns:
            columns.append(col)

    st.dataframe(
        sentiment[columns],
        use_container_width=True,
        hide_index=True
    )

else:

    st.warning("No Sentiment Data")

st.markdown("---")

# -------------------- PREDICTIONS -------------------- #

st.subheader("📈 Market Predictions")

if not prediction.empty:

    columns = []

    for col in [
        "stock",
        "prediction",
        "impact_score"
    ]:
        if col in prediction.columns:
            columns.append(col)

    st.dataframe(
        prediction[columns],
        use_container_width=True,
        hide_index=True
    )

else:

    st.info("No Prediction Data Found")

st.markdown("---")

# -------------------- DOWNLOAD -------------------- #

if not news.empty:

    csv = news.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download News CSV",
        data=csv,
        file_name="financial_news.csv",
        mime="text/csv",
        key="download_csv"
    )

st.success("✅ Dashboard Loaded Successfully")
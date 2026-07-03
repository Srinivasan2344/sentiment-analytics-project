import plotly.express as px
import pandas as pd


def sentiment_pie(sentiment_df):

    if sentiment_df.empty:
        return px.pie(title="No Data")

    counts = sentiment_df["sentiment"].value_counts().reset_index()
    counts.columns = ["Sentiment", "Count"]

    fig = px.pie(
        counts,
        names="Sentiment",
        values="Count",
        hole=0.5,
        title="Sentiment Distribution"
    )

    return fig


def company_chart(news_df):

    if news_df.empty:
        return px.bar(title="No Data")

    company = news_df["company"].fillna("Unknown").value_counts().reset_index()
    company.columns = ["Company", "News Count"]

    fig = px.bar(
        company,
        x="Company",
        y="News Count",
        title="Company-wise News Count"
    )

    return fig


def trend_chart(news_df):

    if news_df.empty:
        return px.line(title="No Data")

    news_df["published_at"] = pd.to_datetime(news_df["published_at"])

    trend = (
        news_df.groupby(news_df["published_at"].dt.date)
        .size()
        .reset_index(name="News Count")
    )

    fig = px.line(
        trend,
        x="published_at",
        y="News Count",
        markers=True,
        title="Daily News Trend"
    )

    return fig
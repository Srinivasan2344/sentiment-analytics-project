from services.sentiment import analyze_sentiment

news = "Apple stock surged after reporting record quarterly earnings."

result = analyze_sentiment(news)

print(result)
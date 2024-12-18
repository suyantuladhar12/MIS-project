
import requests
import json
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

API_ENDPOINT = "https://newsdata.io/api/1/latest"
API_KEY = "" # Enter your API key here.
COUNTRY_CODE = "NP"  

def fetch_news(api_endpoint, api_key, country_code):
    params = {
        "apikey": api_key,
        "country": country_code
    }
    response = requests.get(api_endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch news: {response.status_code}")
        return None

def analyze_sentiment(headlines):
    results = []
    for headline in headlines:
        title = headline.get("title", "")
        description = headline.get("description", "")

        sentiment_scores = sia.polarity_scores(title)

        if sentiment_scores['compound'] >= 0.05:
            sentiment_label = "Positive"
        elif sentiment_scores['compound'] <= -0.05:
            sentiment_label = "Negative"
        else:
            sentiment_label = "Neutral"

        results.append({
            "title": title,
            "description": description,
            "sentiment_scores": sentiment_scores,
            "sentiment_label": sentiment_label
        })
    return results

def save_to_json(data, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    news_data = fetch_news(API_ENDPOINT, API_KEY, COUNTRY_CODE)
    if news_data and "results" in news_data:
        headlines = news_data["results"]
        analyzed_data = analyze_sentiment(headlines)
        save_to_json(analyzed_data, "news_sentiment_results.json")
        print("Sentiment analysis completed. Results saved to 'news_sentiment_results.json'.")
    else:
        print("No news data found.")



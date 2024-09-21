import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key and base URL from environment variables
API_KEY = os.getenv('API_KEY')
BASE_URL = os.getenv('BASE_URL')


def get_top_headlines(api_key, country='us', category='general'):
    # Define the parameters for the API request
    params = {
        'apiKey': api_key,
        'country': country,
        'category': category,
        'pageSize': 5  # Number of results to return
    }

    # Send the request to the NewsAPI endpoint
    response = requests.get(BASE_URL, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        articles = data.get('articles', [])
        return articles
    else:
        print(f"Error fetching data: {response.status_code}")
        return []


def main():
    articles = get_top_headlines(API_KEY)

    # Print out the top headlines
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Source: {article['source']['name']}")
        print(f"Published At: {article['publishedAt']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}\n")


if __name__ == "__main__":
    main()

import requests

# Replace 'your_api_key_here' with your actual NewsAPI key
API_KEY = '5ce070126d2c4e04bedd101eea14ca36'
BASE_URL = 'https://newsapi.org/v2/top-headlines'


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

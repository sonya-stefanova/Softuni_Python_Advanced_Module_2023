import requests

# API endpoint
url = 'https://newsapi.org/v2/everything?q=SEO?&apiKey=46142bef6bd54a2f8b03f6d9b928ca44'

# Make request to the API
response = requests.get(url)

# Get the response data as a python object
seo_data = response.json()

articles_counter = 1

for article in seo_data['articles']:
    if articles_counter <= 10:
        print(f"{articles_counter}: {article['title']}\n{article['description']}\nCheck more here:{article['url']}")
        articles_counter += 1
    else:
        break

# na razie dodane
import requests as req

import sql
from article import Article


api_data = sql.get_api_data()
api_key = api_data[0]['api_key']
api_url = api_data[0]['api_url']

# requests.get(url, params={key: value}, args)
request = req.get(api_url, params={'q': 'tesla', 'apiKey': api_key})
article_json = request.json()

# Dodawanie do modelu
# data_disc = json.load(article_json)
articles = [Article(**data) for data in article_json['articles']]

# Dodanie do bazy danych przy użyciu klas
for article in articles:
    sql.add_to_database(article.author, article.title, article.description, article.url, article.urlToImage, article.publishedAt, article.content)

# Zapisanie do pliku
file_path = "artykul.txt"
with open(file_path, 'w') as file:
    file.write(request.text)

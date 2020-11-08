import requests
import json

API_KEY = "27bd1bb9af0b4379852de8226697827d"


def return_list(url):
    data = requests.get(url)
    diction_load = json.loads(data.content)

    List = []
    if diction_load['status'] == "error":
        print("error")
    articles = diction_load['articles']
    for item in articles:
        dictionary = {}
        dictionary['author'] = item['author']
        dictionary['title'] = item['title']
        dictionary['url'] = item['url']
        dictionary['imageSrc'] = item['urlToImage']
        dictionary['time'] = item['publishedAt']
        List.append(dictionary)
    return List


def top_headlines_search(search):
    search_top_headlines = "https://newsapi.org/v2/top-headlines?q=" + search + "&apiKey=" + API_KEY
    List = return_list(search_top_headlines)
    print(List)
    return List


def get_top_headlines_category(category):
    country = "in"
    top_headlines_category = "https://newsapi.org/v2/top-headlines?country=" + country + "&category=" + category + "&apiKey=" + API_KEY
    List = return_list(top_headlines_category)
    print(List)


def get_news_from_source(source):
    top_headlines_src = "https://newsapi.org/v2/top-headlines?sources=" + source + "&apiKey=" + API_KEY
    List = return_list(top_headlines_src)
    print(List)


def get_top_headlines_country(country):
    country = country
    top_headlines_country = "https://newsapi.org/v2/top-headlines?country=" + country + "&apiKey=" + API_KEY
    List = return_list(top_headlines_country)
    print(List)

# определяем список хабов, которые нам интересны
TARGET_WORDS = ['дизайн', 'фото', 'web', 'python']

import requests
from bs4 import BeautifulSoup
from pprint import pprint


url = 'https://habr.com/ru/articles/'
ret = requests.get(url)
soup = BeautifulSoup(ret.text, 'html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')
for article in articles:
    preview1 = article.find_all(class_ = "article-formatted-body article-formatted-body article-formatted-body_version-1")
    preview2 = article.find_all(class_ = "article-formatted-body article-formatted-body article-formatted-body_version-2")
    date = article.find('a', class_='tm-article-datetime-published').find('time').get('title')
    title = article.find('h2', class_="tm-title tm-title_h2").get_text(strip=True)
    link = article.find('a', class_="tm-title__link").get('href')
    
    
    
    for word in TARGET_WORDS:
        if word in preview1 or word in preview2:
            result = f'{date} - {title} - {url}{link}'
            print(result)

    

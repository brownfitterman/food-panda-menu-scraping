from bs4 import BeautifulSoup
import requests
url="https://www.foodpanda.my/"
html =  requests.get(url)

soup=BeautifulSoup( html.text,'lxml')

rests=soup.find('ul',class_='city-list')

list_1=rests.find_all('li')
for url in list_1:
    url_city=url.find('a',class_='city-tile')['href'].strip()
    print(len(url_city))
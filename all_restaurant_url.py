from bs4 import BeautifulSoup
import requests
url="https://www.foodpanda.my/city/bayan-baru"
html =  requests.get(url)
soup=BeautifulSoup( html.text,'lxml')
rests=soup.find('ul',class_='vendor-list')


list_1=rests.find_all('a',class_='hreview-aggregate url')


for url in list_1:
   url=str(url)
   url=(((url.split())[5]).split('='))[1]
   url=url[1:-2]
   print(url)



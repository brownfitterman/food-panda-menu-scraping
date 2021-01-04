from bs4 import BeautifulSoup
import requests



url="https://www.foodpanda.my"
html =  requests.get(url)

soup=BeautifulSoup( html.text,'lxml')

rests=soup.find('ul',class_='city-list')

all_c_all_r=[]
url_cities=[]

list_1=rests.find_all('li')
for url in list_1:
    url_city=url.find('a',class_='city-tile')['href'].strip()
    url_cities.append(url_city)


for element in url_cities:
    print(element[6:], 'done')
    url="https://www.foodpanda.my"+element
    html =  requests.get(url)
    soup=BeautifulSoup( html.text,'lxml')
    rests=soup.find('ul',class_='vendor-list')

    try:
        list_1=rests.find_all('a',class_='hreview-aggregate url')
    except:
        pass

    for url in list_1:
        url=str(url)
        url=(((url.split())[5]).split('='))[1]
        url=url[1:-2]
        all_c_all_r.append(url)
        


print(all_c_all_r)


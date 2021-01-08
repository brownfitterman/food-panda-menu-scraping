from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

restaurant_full_name=[]
restaurant_url=[]
dish_category_title=[]
dish_name=[]
dish_description=[]
original_price=[]
discounted_price=[]
image_url=[]
all_r=[]

print('Welcome to Food Panda Menu Scrapper!')
print()
print('Food Panda Malaysia')
print()

print()

rest_url=input('Enter a Restaurant URL to scrape its menu: ')

html =  requests.get(rest_url)

soup=BeautifulSoup( html.text,'lxml')

item=soup.find_all('div',class_='dish-category-section__inner-wrapper')


h1=soup.find('h1',class_='fn')    #to get restaurant name 
restaurant_name=h1.text



for data in item:
    pic=data.find_all('li',class_='dish-card h-product menu__item')
    for img in pic:
        image=img.find('div',class_='photo u-photo b-lazy')
        if image is None:
            print('N/A')
        else:
            image=str(image)
            image=image[image.find('data-src')+9:]
            image=(image.split('?'))[0]
            image=image[1:]
            print(image)


from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
url="https://www.foodpanda.my/chain/cb0hc/domino-s-pizza-pos-integration"
html =  requests.get(url)

soup=BeautifulSoup( html.text,'lxml')

item=soup.find_all('div',class_='dish-category-section__inner-wrapper')

dish_category_title=[]
dish_name=[]
original_price=[]
discounted_price=[]
image_url=[]

for data in item:
    h2=data.find('h2',class_='dish-category-title').text.strip()
    titles=data.find_all('h3',class_='dish-name fn p-name')
    for title in titles:
        dish_category_title.append(h2)
        item=title.text.strip()
        dish_name.append(item)
        

    prices=data.find_all('span',class_='price p-price')
    for price in prices:
        price=str(price)
        price=price.split()
        dis_price=price[-4]
        org_price=price[-2]
        org_price=(((org_price.split('>'))[1]).split('<'))[0]
        try:
            x=price.index('from')
            dis_price="from"+dis_price
        except:
            pass
        original_price.append(org_price)
        discounted_price.append(dis_price)
        
    images=data.find_all('picture')
    for img in images:
        img=str(img)
        img=((img.split())[5]).split('=')
        img=(((img[1])[1:]).split('?'))[0]
        image_url.append(img)

# now lists are made for the categories
#we will now use the lists as pandas series and create a pandas dataframe

df=pd.DataFrame({'dish_category_title':dish_category_title,
'dish_name':dish_name,
'original_price':original_price,
'discounted_price':discounted_price,
'image_url':image_url})

print(df.head())



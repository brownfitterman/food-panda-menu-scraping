from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

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


h1=soup.find('h1',class_='fn')
restaurant_name=h1.text



for data in item:
    h2=data.find('h2',class_='dish-category-title').text.strip()
    titles=data.find_all('h3',class_='dish-name fn p-name')
    for title in titles:
        dish_category_title.append(h2)
        item=title.text.strip()
        dish_name.append(item)
        

    title_descs=data.find_all('div',class_='dish-info')
    for title_desc in title_descs:       
        try:
           desc=title_desc.find('p',class_='dish-description e-description').text.strip()
        except:
            desc="Dish Description not available"
        dish_description.append(desc)


    prices=data.find_all('span',class_='price p-price')
    for price in prices:
        price=str(price)
        price=price.split()
        dis_price=price[-4]
        if "MYR" not in dis_price:
            dis_price="N/A"
        try:
            org_price=price[-2]      
            org_price=(((org_price.split('>'))[1]).split('<'))[0]
        except:
            org_price=price[-2] 
            
        try:
            x=price.index('from')
            dis_price="from "+dis_price
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

if (len(image_url)!=len(dish_name)):
    image_url=[]
    for i in range(len(dish_name)):
        image_url.append("N/A")


df=pd.DataFrame({'dish_category_title':dish_category_title,
'dish_name':dish_name,
'dish_description':dish_description,
'original_price':original_price,
'discounted_price':discounted_price,
'image_url':image_url})

filename=restaurant_name.replace(' ','_')+"_menu.csv"
df.to_csv(filename)

print()
print()
print(restaurant_name+"'s Menu scraped successfully!")
print('Exported to csv')
print('Check '+filename)
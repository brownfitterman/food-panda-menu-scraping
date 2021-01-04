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
print('Food Panda is available in these cities of Malaysia:')
print()

htm =  requests.get("https://www.foodpanda.my/")

soup0=BeautifulSoup( htm.text,'lxml')

rests0=soup0.find('ul',class_='city-list')

list_0=rests0.find_all('li')
y=0
for url in list_0:
    url_city=url.find('a',class_='city-tile')['href'].strip()
    cityname=url_city[6:]
    print(cityname, end='')
    for z in range(20-len(cityname)):
        print(' ',end='')
    y=y+1
    if (y%5==0):
        print()
    
print()
print()
cityname=input('Enter a City Name to get the restaurants info of that city:')
url="https://www.foodpanda.my/city/"+cityname
html =  requests.get(url)
soup=BeautifulSoup( html.text,'lxml')
rests=soup.find('ul',class_='vendor-list')

try:
    list_1=rests.find_all('a',class_='hreview-aggregate url')
except:
    pass
y=0
dct={}
for url in list_1:
    url=str(url)
    url=(((url.split())[5]).split('='))[1]
    url=url[1:-2]
    all_r.append(url)
    restaur_name=url[17:]
    dct[restaur_name]= url[:17]
    restaur_name=restaur_name.rstrip()
    # print(restaur_name)
    print(restaur_name, end='')
    for z in range(50-len(restaur_name)):
        print(' ',end='')
    y=y+1
    if (y%3==0):
        print()
    
print()
print()
total_rests=len(all_r)        
print('There are total '+ str(total_rests)+ ' restaurants in '+cityname+'.')

print()
u=0

chosen_rest=input('Enter a Restaurant Name to scrape its menu: ')

url="https://www.foodpanda.my"+dct[chosen_rest]+chosen_rest
html =  requests.get(url)

soup=BeautifulSoup( html.text,'lxml')

item=soup.find_all('div',class_='dish-category-section__inner-wrapper')



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

filename=chosen_rest+"_menu.csv"
df.to_csv(filename)

print()
print()
print("Menu scraped successfully!")
print('Exported to csv')
print('Check '+filename)
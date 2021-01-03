from bs4 import BeautifulSoup
import requests
import csv
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
    #print('h2=',h2)
    # para=data.find('p',class_='dish-category-description').text.strip()
    titles=data.find_all('h3',class_='dish-name fn p-name')
    for title in titles:
        dish_category_title.append(h2)
        item=title.text.strip()
        #print('title=',item)
        dish_name.append(item)
        
   
    # photo=data.find('div',class_='photo u-photo b-lazy b-loaded')['data-src']
    prices=data.find_all('span',class_='price p-price')
    for price in prices:
        price=str(price)
        price=price.split()
        dis_price=price[-4]
        org_price=price[-2]
        org_price=(((org_price.split('>'))[1]).split('<'))[0]
        #print('dis_price=', end="")
        try:
            x=price.index('from')
            #print(' from ', end="")
            dis_price="from"+dis_price
        except:
            pass
        #print(dis_price, ',  org_price=',org_price)
        original_price.append(org_price)
        discounted_price.append(dis_price)
        
    images=data.find_all('picture')
    for img in images:
        img=str(img)
        img=((img.split())[5]).split('=')
        img=(((img[1])[1:]).split('?'))[0]
        #print(img)
        image_url.append(img)



print(dish_category_title)
print()
print(dish_name)
print()
print(original_price)
print()
print(discounted_price)
print()
print(image_url)
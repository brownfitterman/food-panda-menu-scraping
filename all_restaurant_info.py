from bs4 import BeautifulSoup
import requests
import csv
url="https://www.foodpanda.my/chain/cf7dm/lan-je-steam-fish"
url=url+"#restaurant-info"
html =  requests.get(url)

soup=BeautifulSoup( html.text,'lxml')

name=[]
address=[]
opening_time=[]
delivery_hours=[]
rating=[]
rating_count=[]
image_url=[]



# data=soup.find_all('script',id_='template-confirm-preorder')
data_all=soup.find_all('div',class_='modal fade rich-description')

for data in data_all:


    img=data.find('div',class_='b-lazy vendor-picture')
    img=str(img)
    img=((img.split())[3]).split('=')
    img=((img[1]).split('?'))[0]
    image_url.append(img)
    
    ven_name=data.find('h1',class_='vendor-name').text.strip() 
    rat=data.find('span',class_='rating').text.strip() 
    count=data.find('span',class_='count').text.strip() 
    name.append(ven_name)  
    rating.append(rat) 
    rating_count.append(count)  #no. of people votes taken for the rating

    # tag=data.find('ul',class_='vendor-cuisines')
    # for tag in tag:
    #     print(tag)
    

        


    timings=data.find('span',class_='schedule-times')
    op_time=timings.text.strip()
    # timing=data.find('span',class_='green-class')
    # timing=timing.text.strip()
    # op_time=timing+" "+op_time
    opening_time.append(op_time)


    hours=data.find('ul',class_='vendor-delivery-times')
    hours=(hours.text.replace(' ','').strip())
    delivery_hours.append(hours)

    
    loc=data.find('p',class_='vendor-location')
    loc=loc.text.strip()
    address.append(loc)


print(name)
print(address)
print(opening_time)
print(delivery_hours)
print(rating)
print(rating_count)
print(image_url)




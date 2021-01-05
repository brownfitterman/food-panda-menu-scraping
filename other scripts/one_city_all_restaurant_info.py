import time
startTime = time.time()

from bs4 import BeautifulSoup
import requests
import csv


all_r=[]



name=[]
address=[]
opening_time=[]
delivery_hours=[]
rating=[]
rating_count=[]
image_url=[]

cityname=input()
url="https://www.foodpanda.my/city/"+cityname
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
    all_r.append(url)
        


for rest_url in all_r:
    print('Restaurant Name: ',rest_url[17:], 'done')
    rest_url="https://www.foodpanda.my"+rest_url+"#restaurant-info"
    html2 =  requests.get(rest_url)

    soup2=BeautifulSoup( html2.text,'lxml')

    # data=soup.find_all('script',id_='template-confirm-preorder')
    data_all=soup2.find_all('div',class_='modal fade rich-description')

    for data in data_all:
        img=data.find('div',class_='b-lazy vendor-picture')
        img=str(img)
        img=((img.split())[3]).split('=')
        img=(((img[1]).split('?'))[0])[1:]
        image_url.append(img)
        
        ven_name=data.find('h1',class_='vendor-name').text.strip() 
        try:
            rat=data.find('span',class_='rating').text.strip() 
        except:
            rat="N/A"
        try:
            count=data.find('span',class_='count').text.strip() 
        except:
            count="N/A"
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



executionTime = (time.time() - startTime)
print()
print()
print('Execution time in seconds: ' + str(executionTime))
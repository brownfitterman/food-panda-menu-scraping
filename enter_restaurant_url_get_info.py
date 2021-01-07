from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

all_r=[]



name=[]
address=[]
opening_time=[]
delivery_hours=[]
rating=[]
rating_count=[]
image_url=[]
longitude=[]
latitude=[]
tags=[]
telephone=[]
postalcode=[]

print('Welcome to Food Panda Menu Scrapper!')
print()
print('Food Panda Malaysia')
print()
print()
rest_url=input('Enter Restaurant URL to get its info: ')
print()
print()



html2 =  requests.get(rest_url)

soup2=BeautifulSoup( html2.text,'lxml')


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



    tag_all_in_one=data.find('ul',class_='vendor-cuisines')
    tag_all_in_one=(tag_all_in_one.text.replace(' ','').strip())
    all_tag_list=tag_all_in_one.split()
    tgs=""

    for each_t in all_tag_list[3:]:
        tgs=tgs+","+each_t
    
    tags.append(tgs)




    timings=data.find('span',class_='schedule-times')
    op_time=timings.text.strip()
    opening_time.append(op_time)


    hours=data.find('ul',class_='vendor-delivery-times')
    hours=(hours.text.replace(' ','').strip())
    delivery_hours.append(hours)

    
    loc=data.find('p',class_='vendor-location')
    loc=loc.text.strip()
    address.append(loc)



script=soup2.find_all('script')[1]
script=str(script)

try:
    longitude_index=script.find('longitude')
    long=script[longitude_index+12:]
    long=(long.split())[0]
    longitude.append(long)


    latitude_index=script.find('latitude')
    lat=script[latitude_index+10:]
    lat=(lat.split())[0]
    lat=lat[:-1]
    latitude.append(lat)
except:
    longitude.append("")
    latitude.append("")


try:
    tel_index=script.find('tel')
    tel=script[tel_index+13:]
    tel=(((tel.split())[0]).split('"'))[0]
    telephone.append(tel)
except:
    telephone.append('')


try:
    postal_index=script.find('postalCode')
    postal=script[postal_index+14:]
    postal=(((postal.split())[0]).split('"'))[0]
    postalcode.append(postal)
except:
    postalcode.append('')





dct=({'Name of Restaurant':name,
'Address':address,
'Opening Time':opening_time,
'Delivery Hours':delivery_hours,
'Rating':rating,
'Rating Count':rating_count,
'Image URL':image_url,
'Longitude':longitude,
'Latitude':latitude,
'Tags': tags,
'Tel No.': telephone,
'Postal Code': postalcode})


for k,v in dct.items():
    print(k+" : "+v[0])
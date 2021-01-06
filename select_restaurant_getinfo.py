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

chosen_rest=input('Enter a Restaurant Name to get its info: ')
print()
print()


rest_url="https://www.foodpanda.my"+dct[chosen_rest]+chosen_rest+"#restaurant-info"
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


try:
    script=soup2.find_all('script')[1]
    script=str(script)

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




dct=({'Name of Restaurant':name,
'Address':address,
'Opening Time':opening_time,
'Delivery Hours':delivery_hours,
'Rating':rating,
'Rating Count':rating_count,
'Image URL':image_url,
'Longitude':longitude,
'Latitude':latitude})


for k,v in dct.items():
    print(k+" : "+v[0])
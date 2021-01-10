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
restaurant_url=[]

htm =  requests.get("https://www.foodpanda.my/")

soup0=BeautifulSoup( htm.text,'lxml')

rests0=soup0.find('ul',class_='city-list')

print('Welcome to Food Panda Restaurants Info Scrapper!')
print()
print('Scraping Food Panda Malaysia Website......')
print()
print()
print('Food Panda is available in these cities of Malaysia:')
print()

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

for url in list_1:
    url=str(url)
    url=(((url.split())[5]).split('='))[1]
    url=url[1:-2]
    all_r.append(url)

total_rests=len(all_r)        
print('There are total '+ str(total_rests)+ ' restaurants in '+cityname+'.')
print('Scraping the info of the restaurants one by one.')
print()
u=0
for rest_url in all_r:
    print(rest_url)
    u=u+1
    rest_name=(rest_url.split('/'))[3]
    print('Restaurant #'+str(u)+' '+ 'Name: '+ rest_name+'  scraped successfully',end=' ')
    for i in range(50-len(rest_name)):
        print(" ",end="")
    print(str(total_rests-u)+" left")
    rest_url="https://www.foodpanda.my"+rest_url+"#restaurant-info"
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
    
    try:
        re_url_index=script.find('url')
        re_url=script[re_url_index+7:]
        re_url=(re_url.split('"'))[0]
        restaurant_url.append(re_url)

    except:
        restaurant_url.append('')


df=pd.DataFrame({'Name of Restaurant':name,
'Address':address,
'Restaurant URL': restaurant_url,
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


filename=cityname+"_restaurants_info.csv"

df.to_csv(filename)

print()
print()
print("All "+ str(total_rests)+ " restaurants info scraped successfully!")
print('Exported to csv')
print('Check '+filename)

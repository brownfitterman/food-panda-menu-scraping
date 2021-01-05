from bs4 import BeautifulSoup
import requests
url="https://www.foodpanda.my/restaurant/o2sy/dominos-pizza-taman-tun"
url=url+"#restaurant-info"
html =  requests.get(url)

soup=BeautifulSoup( html.text,'lxml')



# data=soup.find_all('script',id_='template-confirm-preorder')
data_all=soup.find_all('div',class_='modal fade rich-description')

for data in data_all:


    img=data.find('div',class_='b-lazy vendor-picture')
    img=str(img)
    img=((img.split())[3]).split('=')
    img=(((img[1]).split('?'))[0])[1:]
    print(img)
    
    ven_name=data.find('h1',class_='vendor-name').text.strip() 
    try:
        rat=data.find('span',class_='rating').text.strip() 
    except:
        rat="N/A"
    try:
        count=data.find('span',class_='count').text.strip() 
    except:
        count="N/A"
    print(ven_name)  
    print(rat) 
    print(count) #no. of people votes taken for the rating

    # tags=data.find('ul',class_='vendor-cuisines')
    # for tag in tags:
    #     li=tag.find('li')
    #     #li=li.text
    #     print(li)
    

        
        
    # timing=data.find('span',class_='green-class')
    # timing=timing.text.strip()
    # print(timing , end='')
    timings=data.find('span',class_='schedule-times')
    time=timings.text.strip()
    print(time)


    hours=data.find('ul',class_='vendor-delivery-times')
    hours=(hours.text.replace(' ','').strip())
    print(hours)

    
    loc=data.find('p',class_='vendor-location')
    loc=loc.text.strip()
    print(loc)



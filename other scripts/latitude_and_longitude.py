from bs4 import BeautifulSoup
import requests
import csv
import json
import pandas as pd

url="https://www.foodpanda.my/restaurant/o8af/warong-makan-makan#"
html =  requests.get(url)

soup=BeautifulSoup( html.text,'lxml')

script=soup.find_all('script')[1]
script=str(script)

longitude_index=script.find('longitude')
longitude=script[longitude_index+12:]
longitude=(longitude.split())[0]


latitude_index=script.find('latitude')
latitude=script[latitude_index+10:]
latitude=(latitude.split())[0]
latitude=latitude[:-1]


print( 'longitude=', longitude)
print( 'latitude=', latitude)
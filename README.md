# Food-Panda-Menu-Scraper
Python Script to scrape the entire menu and info of all restaurants of Food Panda.
The scraping is done using Beautiful Soup and Requests.

There are six scripts:

1. enter_restaurant_url_get_info.py   : enter the url of the restaurant and get info of restaurant in terminal
2. enter_restaurant_url_get_menu.py   : enter the url of restaurant and get the menu of the restaurant in csv file
3. one_city_all_restaurant_info_csv.py: runnning the script returns name of all cities, enter a city and info of all restaurants of that city will be exported to a csv file
4. select_city_getmenu.py             : runnning the script returns name of all cities, enter a city and menu of all restaurants of that city will be exported to a csv file
5. select_restaurant_getinfo.py       : runnning the script returns name of all cities, enter a city, it returns name of all restaurants of that city, enter a restaurant and info of all restaurants of that city will be exported to a csv file
6. select_restaurant_getmenu.py       : runnning the script returns name of all cities, enter a city, it returns name of all restaurants of that city, enter a restaurant and menu of all restaurants of that city will be exported to a csv file


The info scripts scrapes the following:
Name of Restaurant
Address
Restaurant URL
Opening Time
Delivery Hours
Rating
Rating Count
Image URL
Longitude
Latitude
Tags
Tel No.
Postal Code

The menu scripts scrapes the following:
Restaurant Name
Restaurant URL
Dish Category Title
Dish Name
Dish Description
Original Price
Discounted Price
Image URL

Made By: Ashutosh Sharma (Github: ashucrma)   &   Dheeraj Joshi (Github: dheeraj009joshi)
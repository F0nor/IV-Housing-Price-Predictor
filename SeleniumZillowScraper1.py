from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# use firefox browser
driver = webdriver.Firefox()
driver.execute_cdp_cmd('Network.setUserAgentOverride', {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/116.0'})

# sets url
target_url = "https://www.zillow.com/santa-barbara-county-ca/rentals/"
driver.get(target_url)

# get html source code and sends end keys to scroll (doesn't do anything for some reason)
html = driver.find_element('tag name', 'html')
html.send_keys(Keys.END)
time.sleep(5)
resp = driver.page_source
driver.close()

# creates empty list and array
l = list()
store = {}

# parses source code and searches for card info
soup = BeautifulSoup(resp,'html.parser')
properties = soup.find_all('div', {'class' : 'StyledPropertyCardDataWrapper-c11n-8-84-3__sc-1omp4c3-0 bKpguY property-card-data'})

# scans through all items (doesn't work as intended; only 9 items are picked up)
for property in range(0,len(properties)):
   
    try:
        store['price'] = str(properties[property].find('span', {'class' : 'PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr'}).text)
    except AttributeError:
        store['price'] = None
    try:
        store['address'] = str(properties[property].find('address', {'data-test' : 'property-card-addr'}).text)
    except AttributeError:
        store['address'] = None
    try:
        store['bed'] = str(properties[property].find("ul", {'class' : 'StyledPropertyCardHomeDetailsList-c11n-8-84-3__sc-1xvdaej-0 eYPFID'}).text)
    except AttributeError:
        store['bed'] = None
    l.append(store)
    store = {}
print(len(properties))
print(l)
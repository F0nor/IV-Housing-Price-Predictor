import os
from bs4 import BeautifulSoup
import pandas as pd
from seleniumwire import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options 
import time

# set browser to firefox, using Kailash's user agent cmd


# attempts to get selenium to go undected; below are solutions that don't work
Firefox_options = Options()
#Firefox_options.add_experimental_option(
 #   "excludeSwitches", ['enable-automation'])

#Firefox_options.add_argument(
 #   "user-agent=Mozilla/5.0 ((Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/116.0")
#Firefox_options.add_argument("--remote-debugging-port=9222")
Firefox_options.add_argument('--disable-blink-features=AutomationControlled')
driver = webdriver.Firefox(options=Firefox_options)

# loops through 10 pages
for page in range(1,10):
    target_url = "https://www.zillow.com/santa-barbara-county-ca/rentals/{}_p/".format(page)
    # sends request for url and grabs html source code
    driver.get(target_url)
    html = driver.find_element('tag name', 'html')
    html.send_keys(Keys.END) # enters end key to scroll (doesn't work as intended)
    time.sleep(5)
    resp = driver.page_source
    driver.close
    
    # create empty list and array
    l = list()
    store = {}
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

print(l)
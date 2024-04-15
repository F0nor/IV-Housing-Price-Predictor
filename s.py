import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.service import Service
import time
import array

#service = Service(executable_path=r'C:\Program Files\GeckoDriver\gecodriver.exe')
#options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
#driver = webdriver.Firefox(service=service, options=options)
driver = webdriver.Firefox()


target_url = "https://www.zillow.com/santa-barbara-county-ca/rentals/"
driver.get(target_url)
html = driver.find_element('tag name', 'html')
html.send_keys("Keys.END")
time.sleep(5)
resp = driver.page_source
driver.close

l = list()
PropObj = pd.DataFrame()
dict = {}
soup = BeautifulSoup(resp,'html.parser')
properties = soup.find_all('li', {'class' : 'ListItem-c11n-8-84-3__sc-10e22w8-0 StyledListCardWrapper-srp__sc-wtsrtn-0 iCyebE gTOWtl'})

print(len(properties))
from bs4 import BeautifulSoup
# import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Creates empty list/array to hold our data and its specific examples
data = list()
example = {}
for page in range(1,7):


# Opens Realtor in Chrome
    chrome_options = Options()
    chrome_options.add_argument("--disable-extensions")
    realtor = 'https://www.realtor.com/apartments/Santa-Barbara_CA/pg-{}'.format(page)
    driver = webdriver.Chrome(options = chrome_options)
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    driver.get(realtor)


# Gets html keys
    html = driver.find_element(By.TAG_NAME, 'html')
    html.send_keys("Keys.END")

# Gets source code
    time.sleep(5)
    resp = driver.page_source
    driver.close()

# Sets up BeautifulSoup for parsing
    soup = BeautifulSoup(resp, 'html.parser')
    properties = soup.find_all("div", {"class": "CardContent__StyledCardContent-rui__sc-7ptz1z-0 kDqsxy card-content card-content"})

# Loops through properties and parses data into our list
    for x in range(0, len(properties)):
        try:
            example['pricing'] = str(properties[x].find("div", {"class": "Pricestyles__StyledPrice-rui__btk3ge-0 kjbIiZ card-price"}).text)
        except AttributeError:
            example['pricing'] = None
        try:
            example['beds'] = str(properties[x].find("li",{"class":"PropertyBedMetastyles__StyledPropertyBedMeta-rui__a4nnof-0 jkAoUn"}).text)
        except AttributeError:
            example['beds'] = None
        try:
            example['baths'] = str(properties[x].find("li", {"class": "PropertyBathMetastyles__StyledPropertyBathMeta-rui__sc-67m6bo-0 hGQdFx"}).text)
        except AttributeError:
            example['baths'] = None
        try:
            example['size'] = str(properties[x].find("li", {"class": "PropertySqftMetastyles__StyledPropertySqftMeta-rui__sc-1gdau7i-0 cYyTDO"}).text)
        except AttributeError:
            example['size'] = None
        try:
            example['type'] = str(properties[x].find("div", {"class": "base__StyledType-rui__sc-108xfm0-0 eLseZM message"}).text)
        except AttributeError:
            example['type'] = None
        try:
            example['address'] = str(properties[x].find("div", {"class": "card-address truncate-line"}).text)
        except AttributeError:
            example['address'] = None
    
        data.append(example)
        example = {}

# Prints our data for validation
print(data)
print(len(data))
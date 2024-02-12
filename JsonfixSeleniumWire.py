from seleniumwire import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time
import json
opts = Options()
opts.headless = True
service = Service(executable_path=r'C:\Utility\BrowserDriver\geckodriver.exe')
opts.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
driver = webdriver.Firefox(service=service, options=opts)


#url of map location
driver.get('https://www.zillow.com/los-angeles-ca-90291/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22%2090291%22%2C%22mapBounds%22%3A%7B%22west%22%3A-118.51555645275879%2C%22east%22%3A-118.41513454724121%2C%22south%22%3A33.96498099798414%2C%22north%22%3A34.021341767884884%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A96127%2C%22regionType%22%3A7%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A14%7D')
time.sleep(2)
count=1
for request in driver.requests:
    if request.url.startswith("https://www.zillow.com/search/GetSearchPageState.htm?"):
            responseBody=json.loads(request.response.body)
            for home in responseBody["cat1"]["searchResults"]["mapResults"]:
                print(count)
                try:
                 print(home["hdpData"]["homeInfo"])
                except:
                 print("No home info "+home["price"])
                count+=1
            break
driver.quit()
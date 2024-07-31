import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("C:\\Users\\aravi\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
# I have given 404 error url (if we remove 'a' then we can see application Up status message)
url = "https://www.clinique.com/a"

#this is for viewing the page
driver.get(url)
time.sleep(3)
driver.close()

#here we are checking the page is up OR Down
response = requests.get(url)

if response.status_code == 200:
    print(f"Application is UP and running,status code: {response.status_code}")
else:
    print(f"Application is down, status code:{response.status_code})")

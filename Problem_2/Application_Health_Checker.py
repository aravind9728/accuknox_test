import time

import requests
from selenium import webdriver

driver = webdriver.Chrome()
#TODO this is for view the page
driver.get("https://www.clinique.com/")
time.sleep(3)
driver.close()

#TODO here we are checking the page is up OR Down
url = "https://www.clinique.com/"

response = requests.get(url)

if response.status_code == 200:
    print("Apllication is UP and running")
else:
    print("Application is down")
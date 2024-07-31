import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

backend_url = 'http://localhost:3000/greet' 
frontend_url = 'http://localhost:8080/'  


# driver = webdriver.Chrome()

service_obj = Service("C:\\Users\\aravi\\AppData\\Local\\Programs\\Python\\Python312\\Scripts\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# here we are getting and printing the backend message 
response = requests.get(backend_url)
backend_message = response.json().get('message')
print(backend_message)

driver.get(frontend_url)
time.sleep(2)

#we are validating the frontend and backend message     
frontend_message = driver.find_element(By.TAG_NAME, "h1").text
assert frontend_message == backend_message
print("Integration test passed!")

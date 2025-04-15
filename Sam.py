from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
import urllib.parse
# Specify the path to the chromedriver executable
chromedriver_path = r"D:\BirthR\chromedriver-win64\chromedriver.exe"

# Set up the ChromeDriver service
service = Service(chromedriver_path)

# Initialize the Chrome WebDriver
driver = webdriver.Chrome(service=service)

try:
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get('http://cusupport:test$@172.25.36.34:631/')
    sel_Printer=driver.find_element(By.XPATH,"//a[contains(text(),'Administration')]").click()
    add_Printer=driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]/form[1]/input[3]").click()
    time.sleep(2)
 
finally:
    driver.close()

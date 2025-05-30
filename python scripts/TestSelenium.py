# from selenium import webdriver


# driver = webdriver.Chrome()
# driver.get('https://selenium.dev/')
# driver.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By


# driver = webdriver.Chrome()

# driver.get('https://selenium.dev/documentation')
# assert 'Selenium' in driver.title

# elem = driver.find_element(By.ID, 'm-documentationwebdriver')
# elem.click()
# assert 'WebDriver' in driver.title

# driver.quit()

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
#options.add_argument("--headless") 
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
sn="MMW-OB1F-PHARMACY1"
try:
  wait = WebDriverWait(driver, 5)
  driver.get("http://172.25.36.36:631")
  driver.get("http://cupsupport:Test123$@172.25.36.36:631")
  driver.maximize_window()
  driver.find_element(By.XPATH, '//a[@href="/admin"]').click() #to click the link <a tag>
  driver.find_element(By.XPATH, '//input[@value="Add Printer"]').click() #input tag
  wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="lpd"]'))).click()
  #driver.find_element(By.XPATH, '//input[@value="lpd"]').click()
  driver.find_element(By.XPATH, '//input[@value="Continue"]').click()
  lpd_input = driver.find_element(By.NAME, "DEVICE_URI")
  lpd_input.clear()
  lpd_input.send_keys(f"lpd://10.91.231.31{sn}")
  driver.find_element(By.XPATH, '//input[@value="Continue"]').click()
  #lpd_name=driver.find_element(By.NAME, "PRINTER_NAME")
  wait.until(EC.presence_of_element_located((By.NAME, "PRINTER_NAME"))).send_keys(sn)
  
  lpd_desc=driver.find_element(By.NAME, "PRINTER_INFO")
  lpd_desc.send_keys(sn)
  lpd_loc=driver.find_element(By.NAME, "PRINTER_LOCATION")
  lpd_loc.send_keys(sn)
  driver.find_element(By.XPATH, '//input[@value="Continue"]').click()
  select_make = wait.until(EC.element_to_be_clickable((By.NAME, "PPD_MAKE")))
  dropdown = Select(select_make) #this is too select the a dropdown like<select name="PPD_MAKE" size="10">
  dropdown.select_by_value("HP")
  driver.find_element(By.XPATH, '//input[@value="Continue"]').click()
  select_model = driver.find_element(By.NAME, "PPD_NAME")
  dropdown = Select(select_model) #this is too select the a dropdown like<select name="PPD_MAKE" size="10">
  dropdown.select_by_value("pxlmono.ppd")
  add_printer_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Add Printer"]')))
  add_printer_button.click()
  driver.find_element(By.XPATH,'//input[@value="Set Default Options"]').click()




  time.sleep(5)
    
finally:
   driver.quit()



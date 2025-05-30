from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
#driver = webdriver.Chrome()
#wait = WebDriverWait(driver, 5)
#driver.get("http://172.25.36.36:631")
#driver.maximize_window()
#driver.get(f"http://cupsupport:Test123$@172.25.36.36:631")


def setup_printer(sn,url):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)
    driver.get(url)
    driver.maximize_window()
    driver.get(f"http://cupsupport:Test123$@{url.split('//')[1]}")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/admin"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Add Printer"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="lpd"]'))).click()
    driver.find_element(By.XPATH, '//input[@value="Continue"]').click()
    lpd_input = wait.until(EC.presence_of_element_located((By.NAME, "DEVICE_URI")))
    lpd_input.clear()
    lpd_input.send_keys(f"lpd://{sn}")
    driver.find_element(By.XPATH, '//input[@value="Continue"]').click()
    wait.until(EC.presence_of_element_located((By.NAME, "PRINTER_NAME"))).send_keys(sn.split("/")[1])
    driver.find_element(By.NAME, "PRINTER_INFO").send_keys("HP LaserJet Pro M202dw")
    driver.find_element(By.NAME, "PRINTER_LOCATION").send_keys(sn.split("/")[1])
    driver.find_element(By.XPATH, '//input[@value="Continue"]').click()
    Select_make = wait.until(EC.presence_of_element_located((By.NAME, "PPD_MAKE")))
    Select(Select_make).select_by_value("HP")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Continue"]'))).click()
    select_model = wait.until(EC.presence_of_element_located((By.NAME, "PPD_NAME")))
    Select(select_model).select_by_value("pxlmono.ppd")
    add_printer_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Add Printer"]')))
    add_printer_button.click()
    wait.until(EC.element_to_be_clickable((By.XPATH,'//input[@value="Set Default Options"]'))).click()
#setup_printer("10.91.101.168/MBO-GF-HEALTHCHKP","http://172.25.36.36:631")
#list=["http://172.25.36.36:631"]
list=["http://172.16.242.127:631","http://172.16.242.128:631","http://172.16.242.129:631","http://172.16.242.130:631","http://172.16.242.131:631","http://172.16.242.132:631","http://172.16.242.133:631","http://172.16.242.134:631"]

for ip in list:
    setup_printer("10.91.37.36/MGD-GF-ER",ip)


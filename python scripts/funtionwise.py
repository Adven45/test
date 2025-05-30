from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

def setup_printer(driver, url, sn):

    # Login and navigate
    driver.get(f"http://cupsupport:Test123$@{url.split('//')[1]}")#"http://172.25.36.36:631"
    driver.maximize_window()

    wait.until(EC.element_to_be_clickable(By.XPATH, '//a[@href="/admin"]')).click()
    driver.find_element(By.XPATH, '//input[@value="Add Printer"]').click()
    driver.find_element(By.XPATH, '//input[@value="lpd"]').click()
    driver.find_element(By.XPATH, '//input[@value="Continue"]').click()

    lpd_input = driver.find_element(By.NAME, "DEVICE_URI")
    lpd_input.clear()
    lpd_input.send_keys(f"lpd://{sn}")
    driver.find_element(By.XPATH, '//input[@value="Continue"]').click()

    driver.find_element(By.NAME, "PRINTER_NAME").send_keys(sn)
    driver.find_element(By.NAME, "PRINTER_INFO").send_keys(sn)
    driver.find_element(By.NAME, "PRINTER_LOCATION").send_keys(sn)
    driver.find_element(By.XPATH, '//input[@value="Continue"]').click()
    wait = WebDriverWait(driver, 5)
    select_make = wait.until(EC.element_to_be_clickable((By.NAME, "PPD_MAKE")))
    Select(select_make).select_by_value("HP")
    driver.find_element(By.XPATH, '//input[@value="Continue"]').click()

    select_model = wait.until(EC.element_to_be_clickable((By.NAME, "PPD_NAME")))
    Select(select_model).select_by_value("pxlmono.ppd")
    add_printer_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Add Printer"]')))
    add_printer_button.click()
    driver.find_element(By.XPATH,'//input[@value="Set Default Options"]').click()
# ---- MAIN EXECUTION ----

driver = webdriver.Chrome()
sn = "10.91.231.31/MMW-OB1F-PHARMACY1"  # or any serial number you want to use

# First server
setup_printer(driver, "http://172.25.36.36:631", sn)

# Optional wait or confirmation
print("First printer setup complete.")

# Second server
setup_printer(driver, "http://172.25.36.38:631", sn)

print("Second printer setup complete.")
driver.quit()

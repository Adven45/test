from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    # Initialize driver
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 5)

    # Open CUPS page
    driver.get("http://172.16.242.134:631")
    driver.maximize_window()

    # Open with credentials (note: may not work in modern browsers)
    driver.get("http://cupsupport:Test123$@172.16.242.134:631")

    # Admin section
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@href="/admin"]'))).click()
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Add Printer"]'))).click()

    # Protocol selection
    wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="lpd"]'))).click()
    driver.find_element(By.XPATH, '//input[@value="Continue"]').click()

    # URI entry
    sn = "172.16.163.122/MHG-LAB-BARCODE5"  # Example serial number or name
    lpd_input = wait.until(EC.presence_of_element_located((By.NAME, "DEVICE_URI")))
    lpd_input.clear()
    lpd_input.send_keys(f"lpd://{sn}")
    driver.find_element(By.XPATH, '//input[@value="Continue"]').click()

    # Printer name, info, location
    wait.until(EC.presence_of_element_located((By.NAME, "PRINTER_NAME"))).send_keys(sn.split("/")[1])
    driver.find_element(By.NAME, "PRINTER_INFO").send_keys("Brother HL-L2360D Printer")
    driver.find_element(By.NAME, "PRINTER_LOCATION").send_keys(sn.split("/")[1])
    driver.find_element(By.XPATH, '//input[@value="Continue"]').click()

    # Select make
    select_make = wait.until(EC.presence_of_element_located((By.NAME, "PPD_MAKE")))
    Select(select_make).select_by_value("Brother")
    driver.find_element(By.XPATH, '//input[@value="Continue"]').click()

    # Select model
    select_model = wait.until(EC.presence_of_element_located((By.NAME, "PPD_NAME")))
    Select(select_model).select_by_value("foomatic:Brother-HL-2060-pxlmono.ppd")
    add_printer_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@value="Add Printer"]')))
    add_printer_button.click()
    driver.find_element(By.XPATH,'//input[@value="Set Default Options"]').click()

    print("Printer installation completed successfully.")

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()

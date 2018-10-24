import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException  # import exceptions
from selenium.common.exceptions import ElementNotVisibleException  # import exceptions

driver = webdriver.Firefox()
driver.get("https://www.trademe.co.nz")
driver.save_screenshot("first_screenshot.png")  # first screenshots

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "searchString")))  # try exception block to check existing element
except NoSuchElementException:
    print("Element not found and test failed")

try:
    elem = driver.find_element_by_id("searchString")  # try exception block to find element
    elem.clear()
    elem.send_keys("books")   # fill up the search line
    elem.send_keys(Keys.RETURN)  # execute searching
    driver.save_screenshot("second_screenshot.png")  # second screenshots
except NoSuchElementException:
    print("Element not found and test failed")

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "FiltersContainer")))  #  explicit waits
except NoSuchElementException:
    print("Element not found and test failed")

try:
    select = Select(driver.find_element_by_id('LocationFilter_regionSelect'))  # find drop-box
    select.select_by_visible_text("Wellington")  # find visible text in drop-box and execute it
    driver.save_screenshot("third_screenshot.png")  # third screenshots
except (NoSuchElementException, ElementNotVisibleException) as e:
    print("Element not found and test failed")

finally:
    time.sleep(5)  # implicit waits.
    driver.close()

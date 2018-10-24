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
driver.get("http://www.ecostore.co.nz/")
driver.save_screenshot("screenshot1.png")  # first screenshots

driver.find_element_by_class_name("home-page")  # home page

featured = driver.find_element_by_id("home-testimonial-cms")  # featured product

sale = driver.find_element_by_partial_link_text("% OFF Everything")  # Special offers

about_us_link = driver.find_element_by_partial_link_text('Our heritage')  # About page
about_us_link.click()

shipping_link = driver.find_element_by_partial_link_text('Shipping')  # Shipping page
shipping_link.click()

shop_link = driver.find_element_by_partial_link_text('Shop')  # Shopping page
shop_link.click()

skin_link = driver.find_element_by_partial_link_text('Baby')  # Any filters such as product filters
skin_link.click()

select = Select(driver.find_element_by_xpath('//*[@id="facetList_216"]//select[1]'))  # find drop-box
select.select_by_visible_text("Sort by price, low to high")  # find visible text in drop-box and execute it


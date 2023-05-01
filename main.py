import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get('https://rozetka.com.ua/')
time.sleep(3)

find_elem = driver.find_element(by=By.NAME, value='search')
time.sleep(3)
find_elem.send_keys('LG')
find_elem.send_keys(Keys.ENTER)
time.sleep(10)

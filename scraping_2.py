import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.yahoo.co.jp")

search_box = driver.find_element_by_name("p")
search_box.send_keys("selenium")
search_box.submit()
time.sleep(5)
driver.close()
driver.quit()

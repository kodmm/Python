import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://ja.wikipedia.org/wiki/SMAP")


search_a = driver.find_element_by_xpath("//div[@class='dablink noprint']/p")
time.sleep(4)

print(search_a.text)
driver.close()
driver.quit()

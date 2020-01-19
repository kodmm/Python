import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https:/www.google.com/')

search_box = driver.find_element_by_name("q")
hoge = input("search")
search_box.send_keys(hoge)
search_box.submit()
time.sleep(5)
driver.close()
driver.quit()

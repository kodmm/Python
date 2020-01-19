import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC%E3%81%AE%E6%BC%AB%E7%94%BB%E4%BD%9C%E5%93%81%E4%B8%80%E8%A6%A7_%E3%81%82%E8%A1%8C")


search_a = driver.find_elements_by_tag_name("li a")
for search in search_a:
    url = search.get_property("title")
    print(url)


driver.close()
driver.quit()

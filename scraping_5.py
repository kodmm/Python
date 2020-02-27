import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://pizzahut.jp/order/pasta-gratin")

#search_a = driver.find_element_by_class_name("AppImage")
time.sleep(3)
search_b = driver.find_elements_by_class_name("menu-name")
time.sleep(2)
search_c = driver.find_elements_by_class_name("ellipsis-text")


for poi,text in zip(search_b, search_c):
   # print('img:' + (hoge.img))
    print('name：' + (poi.text))
    print('body：' + (text.text))

driver.close()
driver.quit()
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.accuweather.com/en/jp/japan-weather")

search_word = driver.find_element_by_name("query")

search_word.send_keys("Saitama-shi")
search_word.submit()

current_temp = []
condition = []
time.sleep(3)
current_temp = driver.find_elements_by_class_name("high")
condition = driver.find_elements_by_class_name("cond")

print ('Condition   : ' + (condition.text))

for date, condition in zip(current_temp, condition):
    print(date, condition)

driver.close()
driver.quit()
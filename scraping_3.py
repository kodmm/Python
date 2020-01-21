from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.accuweather.com/en/jp/japan-weather")

search_word = driver.find_element_by_name("query")

search_word.send_keys("Saitama-shi")
search_word.submit()

currrent_temp = drive.find_element_by_class_name("high")
condition = driver.find_element_by_class_name("cond")

for name in zip(current_temp, conditon):
    print(name)


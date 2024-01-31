from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://github.com/"
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.com-homepage.png")

url = "http://github.com/sadikturan"
driver.get(url)

print(driver.title)

if "sadikturan" in driver.title:
    driver.save_screenshot("girhub-sadikturan.png")

time.sleep(2)

driver.back() #sayfayı geriye aldık.
# driver.forward() #sayfayı ileri alır.

time.sleep(2)
driver.close()
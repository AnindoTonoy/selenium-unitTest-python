from selenium import webdriver
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.python.org/")
print(driver.title)
driver.close()

# driver.quit() # for exit the browser

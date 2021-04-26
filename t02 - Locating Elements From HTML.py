# Tutorial #2 - Locating Elements From HTML

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://www.python.org/")
print(driver.title)

search = driver.find_element_by_id("id-search-field")
search.send_keys("snake")
search.send_keys(Keys.RETURN)

# codes for Explicit Waits
try:
    search_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "list-recent-events"))
    )

    # codes for printing all the search result's header
    articles = search_result.find_elements_by_tag_name("li")
    for article in articles:
        header = article.find_element_by_tag_name("h3")
        print(header.text)
    
    # print(search_result.text)

finally:
    driver.quit()




# print(driver.page_source)
# time.sleep(10)

# driver.quit()
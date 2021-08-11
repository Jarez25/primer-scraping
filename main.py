'''primer wedscreaping prueba V1'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select

wedside = 'https://www.adamchoi.co.uk/teamgoals/detailed'

path = 'C:/Users/Jarez/Downloads/chromedriver_linux64/chromedriver.exe'

driver = webdriver.Chrome(path)
driver.get(wedside)

machets = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
machets.click()

list_des = Select(driver.find_element_by_id("country"))
list_des.select_by_visible_text("Argentina")

parts = driver.find_elements_by_tag_name("tr")

for part in parts:
    print(part.text)
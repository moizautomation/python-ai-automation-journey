#Day 13  & 14 Selenium Learning
import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# create driver (open browser)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# open website 
#task 2
# driver.get("https://example.com")
# heading = driver.find_element(By.TAG_NAME,"h1")
# para = driver.find_element(By.TAG_NAME,"p")
# print(f"Heading: {heading.text}\nParagraph: {para.text}")

#task 3 (Search Automation)
# driver.get("https://www.wikipedia.org")
# #finding the search bar
# search = driver.find_element(By.NAME,"search")
# #to type in the search bar
# search.send_keys("Python")
# #to press enter
# search.submit()

#task 4 (Extract data from search results)
# driver.get("https://www.wikipedia.org")
# #finding the search bar
# search = driver.find_element(By.NAME,"search")
# #to type in the search bar
# search.send_keys("Python")
# #to press enter
# search.submit()
# #this will wait for 2s ,we added so page can be loaded
# #and the complete header can be extracted

# time.sleep(3)

# heading = driver.find_element(By.TAG_NAME,"h1")
# para = driver.find_element(By.TAG_NAME,"p")
# print(f"Heading: {heading.text}\nParagraph: {para.text}")

#Day 14 (Login Automation)
# driver.get("https://www.saucedemo.com/")
# username = driver.find_element(By.ID,"user-name")
# username.send_keys("standard_user")
# password = driver.find_element(By.ID,"password")
# password.send_keys("secret_sauce")
# login = driver.find_element(By.ID,"login-button")
# login.click()
# time.sleep(3)
#task 2 (extract single product details)
# description = driver.find_element(By.CLASS_NAME,"inventory_item_description")
# print(f"Description: {description.text}")

# #task 3 extract all product data
# #this will return a list of all products
# listm = driver.find_elements(By.CLASS_NAME,"inventory_item")
# #for each product
# for el in listm:
#     #extract its title
#     title = el.find_element(By.CLASS_NAME,"inventory_item_label")
#     print(title.text)

#Day 15 Task 1 (Selenium)
# goals:
# Open the page
# Find both checkboxes
# Check their current state (checked or unchecked)
# Click both checkboxes to change their state
# Verify their new state after clicking
#save any of the checkbox state in csv file

driver.get("https://the-internet.herokuapp.com/checkboxes")

checkboxes = driver.find_elements(By.TAG_NAME,"input")
i = 1
with open("checkbox.csv","w",newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Checkbox",  "Before",  "After"])
    for checkbox in checkboxes:
        before = checkbox.is_selected()
        checkbox.click()
        time.sleep(1)
        After = checkbox.is_selected()
        writer.writerow([i,  before,  After])
        i += 1


    

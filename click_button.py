"""
Two-Step Process:
Find the element using find_element()
Click the element using .click() method
Click Method Syntax
Option 1: Single Line (Chained)
driver.find_element(By.XPATH, "//button[@aria-pressed='false']").click()
Option 2: Two Separate Lines
element = driver.find_element(By.XPATH, "//button[@aria-pressed='false']")
element.click()
Both approaches work identically - choose based on preference and readability

Complete Click Script Template
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

# Create driver
driver = webdriver.Chrome()

# Open page
driver.get("SERVER_URL")

# Wait for page to load
time.sleep(2)

# Find and click element
driver.find_element(By.XPATH, "//button[@aria-pressed='false']").click()

# Wait to see results
time.sleep(2)

# Close browser
driver.quit()
"""
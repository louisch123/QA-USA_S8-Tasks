"""
WAITS
Types of Waits
1. Explicit Waits
Definition: Waits for a specific condition to be met, up to a maximum time limit

Required Import:

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
Basic Syntax:

WebDriverWait(driver, 3)  # Wait up to 3 seconds
With Conditions:

WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.TAG_NAME, "button")))
Common Explicit Wait Conditions:
1. Element Clickable:

expected_conditions.element_to_be_clickable((By.ID, "submit-btn"))
2. Element Present:

expected_conditions.presence_of_element_located((By.CLASS_NAME, "result"))
3. Element Visible:

expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='popup']"))
2. Implicit Waits
Definition: Sets a default wait time for ALL element-finding operations

Syntax:

driver.implicitly_wait(3)  # Apply 3-second wait to all subsequent operations
Behavior:

Set once, applies to all find_element() calls
Waits up to specified time for element to appear in DOM
Continues immediately when element is found
Example:

driver.implicitly_wait(3)
driver.find_element(By.TAG_NAME, "button")    # Waits up to 3 seconds
driver.find_element(By.TAG_NAME, "div")       # Waits up to 3 seconds
driver.find_element(By.TAG_NAME, "input")     # Waits up to 3 seconds
3. Sleep (Static Wait)
Definition: Fixed pause regardless of conditions

Syntax:

import time
time.sleep(3)  # Always waits exactly 3 seconds
Wait Comparison
"""
#EXAMPLE SCRIPT
"""
Complete Example Script
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# Create driver
driver = webdriver.Chrome()

# Set implicit wait (applies to all find operations)
driver.implicitly_wait(5)

# Open page
driver.get("https://example.com")

# Explicit wait for specific condition
WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "submit-button")))

# Click the button
driver.find_element(By.ID, "submit-button").click()

# Static sleep to observe results
time.sleep(2)

# Close browser
driver.quit()
"""
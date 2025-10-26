# send_keys() Method - allow test to be performed in input fields by specifying
# the input in the parentheses
"""
Task Included
Fill in the “From” and “To” fields (locate these fields using their id).
Click the “Call a taxi” button (locate this button using its XPath).
Wait for the comment field to load. Use an explicit wait of 3 seconds until the e
element id="comment" is visible on the page.
Write any comment for the driver.
Use assert to check that the entered comment matches your expected text.
Retrieve the comment using the get_attribute("value") method.
"""
"""
Example:
    Using the "from" and "to" field in the Urban Routes app
"""
# First, find the elements by using driver.find_element(By.ID,)
# then add the .send_keys() method
'Entire Code with task'
"""
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait #Task
from selenium.webdriver.support import expected_conditions #Task
import time

driver = webdriver.Chrome()
driver.maximize_window() #Full Screen
expected_comment = "Please bring a blanket. Thank you."

# We replace with our own URL
driver.get(" https://cnt-7b06106f-eb78-45a3-8079-463faf2f89b2.containerhub.tripleten-services.com/")

# Give the page time to load
time.sleep(2)

# Current URL and saves it
current_url = driver.current_url # obtains the url and saves it

# verify if url in the current url once
assert 'tripleten-services.com' in driver.current_url


#Enter the from address
driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")

# Pause for a second (to view the result)
time.sleep(5)

# Enter the to address
driver.find_element(By.ID, "to").send_keys("1300 1st St")

# Pause for a second (to view the result)
time.sleep(5)


# Click "Call Taxi" button -Task
driver.find_element(By.XPATH, "//button[@class='button round']").click()

#Explicit wait for the comment field - Task
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.ID, "comment")))

#Write a comment - Task
driver.find_element(By.ID, "comment").send_keys(expected_comment)
#Checks that what was typed matches what was expected
assert driver.find_element(By.ID, "comment").get_attribute("value") == "Please bring a blanket. Thank you."

#Removing the "from" address info with .clear()
driver.find_element(By.ID, "from").clear()

#Pause to view result
time.sleep(10)

driver.find_element(By.ID, "from").send_keys("East")

#Pause to view results
time.sleep(10)

# Quit the app
driver.quit()
"""
"In the example above, time.sleep method is used to allow for more viewing load time over waites" \
"which moves through the automation quickly for anyone to notice"

#Using clearing fields to remove text information or correct it during automation
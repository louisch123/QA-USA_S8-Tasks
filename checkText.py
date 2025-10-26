"""
.Text Method
Used at the end of a driver.find_element statement to confirm the text is displayed and correctly spelled
SYNTAX
driver.find_element(By.CLASS_NAME, "logo-disclaimer").text
"""
"Example"
"""
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait #Task
from selenium.webdriver.support import expected_conditions as EC #Task

import time

driver = webdriver.Chrome()

try:
# Replace our link with your own server link here
    driver.get("https://cnt-1e748c9d-1c27-43a3-80ea-db62ee784537.containerhub.tripleten-services.com/")

# Current URL and saves it
    current_url = driver.current_url # obtains the url and saves it

# verify if url in the current url once
    assert 'tripleten-services.com' in driver.current_url

    time.sleep(5)


#Enter the from address -Task
    driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")
#Waits for item to load-Task
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "from")))

# Enter the to address-Task
    driver.find_element(By.ID, "to").send_keys("1300 1st St")
#Waits for item to load - Task
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "to")))

# Gets elements text -Task
    mode = driver.find_element(By.XPATH, "//div[@class='mode active']").text

    time.sleep(5)

# Gets the element's text
    disclaimer = driver.find_element(By.CLASS_NAME, "logo-disclaimer").text

# Assert that the text of the disclaimer and mode variable is "PLATFORM" and "Fastest"
    assert disclaimer == "PLATFORM"
    assert mode == "Fastest"#Task

    print(disclaimer)
    print(mode)
except Exception as e:
    print(f"Error occurred: {e}")

driver.quit()
"""
"""
TASK
Verify that the “Fastest” mode is selected by default after entering the addresses.

The selected mode has a mode active class. You need to make sure that the selected mode contains the text “Fastest.”

You'll find the template for this task in the get_text.py file.
"""
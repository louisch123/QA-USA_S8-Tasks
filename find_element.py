"""
Execution of these statements in openingDriver file
"""
#Two Methods for finding Elements
'.find_element()' # Finding a single element, will return a Webelement object on a web page
'.find_elements()'# Finding multiple elements, will retuns several elements in a list.
#Both require arguments passing with the By. class ahead of an Xpath or an HTML tag

#By. class - Helps to specify search criteria for elements, also needs to be imported
"""
EXAMPLES:

By.ID # Search by the id attribute
By.NAME # Search by the name attribute
By.CLASS_NAME # Search by the class attribute name
By.TAG_NAME # Search by the HTML tag

By.CSS_SELECTOR # Search by the CSS selector
By.XPATH # Search by XPath
"""
#By. class method examples in Urban Routes App
"""
# Finding element by the ID - "from"
driver.find_element(By.ID, "from")

# Finding element by the NAME - "firstName"
driver.find_element(By.NAME, "firstName")

# Finding element by the CLASS_NAME - "button round"
driver.find_element(By.CLASS_NAME, "card-number")

# Finding element by the TAG_NAME - "title"
driver.find_element(By.TAG_NAME, "title")

# Finding element by the CSS_SELECTOR - "input#from" or "input[id='from']"
driver.find_element(By.CSS_SELECTOR, "input#from")

# Finding element by the XPATH - "//input[@id='from']"
driver.find_element(By.XPATH, "//input[@id='from']")
"""
#Once the element is found and the expression is created, the get_attribute() is used in the print()
"""
# Find the element
element = driver.find_element(By.CSS_SELECTOR, ".type-icon")

# Access its attribute
print(element.get_attribute('class'))

# Output: 'type-icon'
"""

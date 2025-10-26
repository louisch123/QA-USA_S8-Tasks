#Using Selenium Opening/Closing pages

import time # loads the built-in time module, which provides various functions for handling time-related tasks

from selenium.webdriver.common.by import By # By. class allows
from selenium import webdriver # WebDrvier
"""
driver= webdriver.Chrome()#Driver
driver.maximize_window()#Full Screen Mode

try: #try/except block to catch errors
    driver.get('https://cnt-d8a90fed-a92e-454f-8951-d3f3d12ddf28.containerhub.tripleten-services.com/') # navigate to url, open page
    time.sleep(20) # controls the length of time to load the page
    current_url = driver.current_url # obtains the url and saves it
    
    elements = driver.find_elements(By.XPATH, "//div[@class='dst-picker-marker']") # Creates an elements variable and
    #finds the element using Xpath
    assert 'tripleten-services.com' in driver.current_url # verify if url in the current url once
    #or use assert current_url == 'https://google.com/' if page needs to be checked multiple times
    assert len(elements) > 1


    element = driver.find_element(By.CSS_SELECTOR, "span.logo-disclaimer") # Creates an element variable and
    # Finds the element using CSS SELECTOR
    driver.find_elements(By.XPATH, "//div[@class='dst-picker-marker']")
    driver.find_element(By.XPATH, "//button[@class='close-button input-close-button']").click() #Click() method

    input_element = driver.find_element(By.ID, "from")#find the input element by its ID
    input_element.send_keys("East")#Simulate user typing "East" into the input field
    time.sleep(5)

except Exception as e:
    print(f"Error occurred: {e}")
print(input_element.get_property("value")) #print property element for the input field
print(element.get_attribute('class')) # Print the found element to the console and access the class
#attribute of the element

driver.quit() #close session

"""
"""Task
Complete the definition of a class for buttons —
Button. All buttons must have the same width — 200 — and the same height — 50./

Complete the __init__ method so that you can create objects with the attributes color (color of the button)
and text (text on the button).

Create two class objects: a yellow and a red button.
The yellow button should have a text variable of "Buy," and the red button should have "Delete."

Print the width and the color of the yellow button and then the width and the color of the red button."""


class Button:
    # Define width and height
    width_button = 200
    height_buttons = 50

    def __init__(self, color, text):  # Complete the __init__ method
        self.button_color = color
        self.button_text = text


# Create a button object with the color 'yellow' and the text 'Buy'
button_1 = Button("yellow", "Buy")
# Create a button object with the color 'red' and the text 'Delete'
button_2 = Button("red", "Delete")

print(button_1.width_button)  # Print the width of the yellow button
print(button_1.button_color)  # Print the color of the yellow button
print(button_2.width_button)  # Print the width of the red button
print(button_2.button_color)  # Print the color of the red button

"""
Task 2
Complete the method is_user_in_group in the Group class: it should check if the user is a member of the group. 
If the user is a member, 
the method should print the following message: "User {name} is in the group".
"""

class User():
    is_registered = True

    def __init__(self, name, login):
        self.user_name = name
        self.user_login = login

    def describe(self):
        return f'Name: {self.user_name}, login {self.user_login}'


class Group():
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, user):
        if user not in self.members:
            print(f'A new member has been added to the group {self.name}')
            self.members.append(user)

    def print_member_descriptions(self):
        print(f'Information about group members {self.name}:')
        for member in self.members:
            print(member.describe())

    def is_user_in_group(self, user):
        # Complete the method
        if user in self.members:
            print(f"User {user.user_name} is in the group")


user1 = User('Mark', 'supermarkus94')
group1 = Group('Dog Lovers')
group1.add_member(user1)
group1.is_user_in_group(user1)


"""
Ch 5 Task
"""
#Task 3
#Write code that finds the “platform” label in the upper left corner of the Urban Routes main page.
# To find this element, write a CSS selector using the element’s class attribute.
#Close the browser after testing.
#You'll find the template in the find_element_exercise_1.py file.
#Answer  driver.find_element(By.CSS_SELECTOR, ".logo-disclaimer") >  Integrated into code aboved

#Task 4
#Write code that finds all the elements with class="dst-picker-marker" on the Urban Routes main page.
#se a relative XPath expression
#To ensure that more than one element has been found, write an assert statement.
#In the statement, use the len() function.
#Answer
# elements = driver.find_elements(By.XPATH, "//div[@class='dst-picker-marker']")
#assert len(elements) > 1, "Expected more than one dst-picker-marker element" > Integrated into code

"""
CH 6 Task
"""
#Practice code
"""
The test should do the following:\

Opens the app.\
Fills out the "To" field\
Fills out the "From" field\
Clicks on the custom "Custom" button.\
Clicks on the "Scooter" button.\
Verifies that the "Scooter" text is displayed.\
"""
"""
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def test_custom_scooter():
    # Create a driver for Chrome
    driver = webdriver.Chrome()

    # Go to the URL - update URL after starting server
    driver.get('https://cnt-533ff756-9131-45bf-848f-17855e154203.containerhub.tripleten-services.com/')

    # Enter From
    driver.find_element(By.ID, 'from').send_keys('East 2nd Street, 601')

    # Enter To
    driver.find_element(By.ID, 'to').send_keys('1300 1st St')

    # Click Custom
    driver.find_element(By.XPATH, '//div[text()="Custom"]').click()
    time.sleep(2)

    # Click Scooter Icon
    driver.find_element(By.XPATH, '//img[@src="/static/media/scooter.cf9bb57e.svg"]').click()
    time.sleep(2)

    # Verify Scooter Text is exists
    actual_value = driver.find_element(By.XPATH, '//div[@class="results-text"]//div[@class="text"]').text
    expected_value = "Scooter"
    assert expected_value in actual_value, f"Expected {expected_value}, but got {actual_value}"

    time.sleep(2)
    # Close the driver
    driver.quit()
"""

"""
import time # loads the built-in time module, which provides various functions for handling time-related tasks

from selenium.webdriver.common.by import By # By. class allows
from selenium import webdriver # WebDrvier

driver= webdriver.Chrome()#Driver
driver.maximize_window()#Full Screen Mode

driver.get(' https://cnt-9f320291-ef5c-4d08-ac72-127bff114d4b.containerhub.tripleten-services.com/') # navigate to url, open page
current_url = driver.current_url # obtains the url and saves it
assert 'tripleten-services.com' in driver.current_url # verify if url in the current url once
#or use assert current_url == 'https://google.com/' if page needs to be checked multiple times

time.sleep(20) # controls the length of time to load the page

element = driver.find_element(By.CSS_SELECTOR, "img.logo-image") # Creates an element variable and
# Finds the element using CSS SELECTOR

input_element = driver.find_element(By.ID, "from")#find the input element by its ID
input_element.send_keys("East")#Simulate user typing "East" into the input field


print(input_element.get_property("value"))
print(element.get_attribute('class')) # Print the found element to the console and access the class
#attribute of the element

driver.quit() #close session
"""
"""
#Along with the webdriver a Driver to manage the browser is needed. A driver is an objec
 #of the WebDriver class. Both are needed to run autotests
"""

#Next Chromeoptions Class to add customized settings, which make opening the browse
#more convenient and in full screen
#Options are optional
"""
chrome_options = webdriver.ChromeOptions() # Create an object for settings
chrome_options.add_argument('--headless') # Add a setting
chrome_options.add_argument('--window-size=640,480') # Add another setting
driver = webdriver.Chrome(options=chrome_options) # Create a driver and pass the settings

'-- headless option' launches the browser w/out showing the window, launches Chrome 
w/out UI. When disabled, the browser window opens when you run the tests , and you 
can see all all the actions automatically performed

'-- window-size' launches the browser with the  specified window size. useful when
you're testing interfaces in systems with a particular screen resolution
"""

# Next get() driver to open pages
"""
Used to navigate to a specified URL and load the web page in the browser window
the page to open will be passed as an argument
"""

#Next create a maximize_window() to maximize the window to full-screen mode
"""
Important because the content can be displayed differently in various window sizes
"""

#Next create a quit() to close the browser after testing is complete
"""
The method kells current session and closes all windows. If the session does not quit
some background processes may fail to shutdown correctly- data leak or access error
"""

#Next obtain the URL of page being tested with current_url method
"""
Obtains and saves the current page url 
"""

#Create an assert() method to confirm the precise url
"""
Assert method will check for url confirmation multiple times
or once depending on how the method is written. 
"""

# Create an import of the  By. class method
""" 
for finding elements using driver.find_element/s() with By. in arguments
"""

# Create a an import for the time. method
"""
This will allow the page to load  fully and execute in selected second intervals
"""

#Create an element variable
"""
The element variable will be used in the print statement arguement
"""

#Create a print statement for the found element
"""
The print statment will pass the found element attributes( class, id, src) that are found in the opening
tag within the double quotes  after the . 
<img src="/static/media/logo_urban.254dc6ec.svg" alt="Routes" class="logo-image" style="width: 171px;">
"""

#Create element properties using get_property()
"""
For input fields, checkboxes, or for elements whose values or states may change dynamically
"""

from selenium.webdriver.common.by import By
from selenium import webdriver
"""
Creating a POM
Step 1. identify the page elements required for the test, such as buttons or input fields. 
This way you know what elements to interact with before creating the page class.
Step 2. After you’ve identified the web elements, you can write the locators.
Step 3. After adding locators, define methods for actions.
"""



#This POM is to validate the functionality of the "Scooter" option in
#Urban Routes App
#Below are the locators and methods

class UrbanRoutesPage:

 # Locators as class attributes (e.g. buttons, text.input fields, img)
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    SCOOTER_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/scooter.cf9bb57e.svg"]')
    SCOOTER_TEXT_LOCATOR = (By.XPATH, '//div[@class="results-text"]//div[@class="text"]')
    BIKE_ICON_LOCATOR = (By.XPATH,'//img[@src="/static/media/bike.fb41c762.svg"]')
    BIKE_TEXT_LOCATOR = (By.XPATH, '//div[@class="results-text"]//div[@class="text"]')
    DRIVE_BUTTON_LOCATOR =(By.XPATH,'(//img[@src="/static/media/car.8a2b1ff5.svg"])[2]')
    BOOK_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button round"]')
    CAMPING_TARIFF_LOCATOR = (By.XPATH, '//div[contains(text(),"Camping")]')
    CAR_MAKE_TEXT_LOCATOR = (By.XPATH, '//div[@class="drive-preview-title"]')
    ADD_DRIVER_LICENSE_LOCATOR = (By.XPATH, '(//div[contains(text(),"Add a driver")])[2]')
    FIRST_NAME_LOCATOR = (By.ID, 'firstName')
    LAST_NAME_LOCATOR = (By.ID, 'lastName')
    DATE_OF_BIRTH_LOCATOR = (By.ID, 'birthDate')
    NUMBER_LOCATOR = (By.ID, 'number')
    ADD_BUTTON_LOCATOR = (By.XPATH, '//button[@type="submit" and text()="Add"]')
    ADD_A_DRIVER_LICENCE_TITLE_LOCATOR = (By.XPATH, '//div[contains(text(),"Add a driver")]')
    VERIFICATION_TEXT_LOCATOR = (By.XPATH, '//div[@class="section active"]//div[@style="margin-bottom: 30px;"]')
 # The new "Duration" text locator
    DURATION_TEXT_LOCATOR = (By.XPATH, '//div[@class="results-text"]//div[@class="duration"]')

# Initialize the driver to contol the web browser with the  __init__ constructor
# this will make it easy to reuse the same driver for multiple actions on the page
    def __init__(self, driver):
        self.driver = driver

#  Methods, def, interact with locators (e.g. clicking, typing, getting text)
#  Unpacking Operator * allows multiple variables/constants to be used with a single name

    def enter_locations(self, from_text, to_text):
        #The methods enter_from_location and enter_to_location are used in sequence
        #in both of our tests and will likely be reused in future tests.
        #combine them into a single method, enter_locations
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
    def choose_camping_car_option(self):
         # Duration Step for "custom_option", "drive_icon", "book button", and "camping"
        self.click_custom_option()
        self.click_drive_button()
        self.click_book_button()
        self.click_camping_option()

         # Step to click "add driver's license"; to enter "first_name", "last_name", "date_of_birth", "number"; and
         # to click "title" and "add button"
    def adding_driver_license(self, first_name, last_name, date_of_birth, number):
        self.click_add_driver_license()
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_date_of_birth(date_of_birth)
        self.enter_number(number)
        self.click_title()
        self.click_add_button()

    def enter_from_location(self, from_text):
        #Enter FROM
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        #Enter TO
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def click_custom_option(self):
        # Click Custom
        self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).click()

# New duration method to combine to methods
    def get_duration_text(self):
        return self.driver.find_element(*self.DURATION_TEXT_LOCATOR).text

    def click_scooter_icon(self):
        # Click Scooter Icon
        self.driver.find_element(*self.SCOOTER_ICON_LOCATOR).click()

    def get_scooter_text(self):
        # Return the "Scooter" text
        return self.driver.find_element(*self.SCOOTER_TEXT_LOCATOR).text

    def click_bike_icon(self):
        # Click Bike Icon
        self.driver.find_element(*self.BIKE_ICON_LOCATOR).click()

    def get_bike_text(self):
        # Return the "Bike" text
        return self.driver.find_element(*self.BIKE_TEXT_LOCATOR).text

    def click_drive_button(self):
        # Click the Drive button
        self.driver.find_element(*self.DRIVE_BUTTON_LOCATOR).click()

    def click_book_button(self):
        # Click the Book Button
        self.driver.find_element(*self.BOOK_BUTTON_LOCATOR).click()

    def click_camping_option(self):
        # Click the Camping tariff option
        self.driver.find_element(*self.CAMPING_TARIFF_LOCATOR).click()

    def get_car_make_text(self):
        # Return the car make text
        return self.driver.find_element(*self.CAR_MAKE_TEXT_LOCATOR).text

    def click_add_driver_license(self):
    # Click Add Driver's Licence
        self.driver.find_element(*self.ADD_DRIVER_LICENSE_LOCATOR).click()


    def enter_first_name(self, first_name):
    # Enter First Name
        self.driver.find_element(*self.FIRST_NAME_LOCATOR).send_keys(first_name)


    def enter_last_name(self, last_name):
    # Enter Last Name
        self.driver.find_element(*self.LAST_NAME_LOCATOR).send_keys(last_name)


    def enter_date_of_birth(self, date_of_birth):
    # Enter Date of Birth
        self.driver.find_element(*self.DATE_OF_BIRTH_LOCATOR).send_keys(date_of_birth)


    def enter_number(self, number):
    # Enter Number
        self.driver.find_element(*self.NUMBER_LOCATOR).send_keys(number)


    def click_title(self):
    # Click Add a Driver's License Title
        self.driver.find_element(*self.ADD_A_DRIVER_LICENCE_TITLE_LOCATOR).click()


    def click_add_button(self):
    # Click Add Button
        self.driver.find_element(*self.ADD_BUTTON_LOCATOR).click()


    def get_verification_text(self):
    # Return the verification text
        return self.driver.find_element(*self.VERIFICATION_TEXT_LOCATOR).text


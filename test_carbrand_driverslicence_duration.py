import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Import the POM class

driver = webdriver.Chrome()#Driver
driver.maximize_window()#Full Screen Mode

# Create a class for both tests
class TestUrbanRoutes:

    def test_drive_custom_camping_option(self):
        driver = webdriver.Chrome()
        driver.get('https://cnt-151a3532-57f2-4c07-993e-2ae63a73dbff.containerhub.tripleten-services.com/')
        # Create an instance of the page class
        urban_routes_page = UrbanRoutesPage(driver)

        # Add implicit waits for web elements to have time to load
        driver.implicitly_wait(3)

        # Choose camping car step to enter "From", "To" and to click "custom_option",
        # "drive_icon", "book button", and "camping"
        urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')
        urban_routes_page.choose_camping_car_option()

        # Check if the text displays "Audi A3 Sedan"
        actual_value = urban_routes_page.get_car_make_text()
        expected_value = "Audi A3 Sedan"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        driver.quit()

    def test_add_driver_license_custom_camping_option(self):
        driver = webdriver.Chrome()
        driver.get('https://cnt-151a3532-57f2-4c07-993e-2ae63a73dbff.containerhub.tripleten-services.com/')

        # Create an instance of the page class
        urban_routes_page = UrbanRoutesPage(driver)
        # Add implicit waits for web elements to have time to load
        driver.implicitly_wait(3)

        # Choose camping car step to enter "From", "To" and to click "custom_option",
        # "drive_icon", "book button", and "camping"
        urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')
        urban_routes_page.choose_camping_car_option()

        # Adding driver license step to click "add driver's license";
        # to enter "first_name", "last_name", "date_of_birth", "number"; and
        # to click "title" and "add button"
        urban_routes_page.adding_driver_license('Anna', 'Smith', '24.04.1889', '01 01 123456')

        # Check that the licence has been added
        actual_value = urban_routes_page.get_verification_text()
        expected_value = "Thank you!"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

        driver.quit()


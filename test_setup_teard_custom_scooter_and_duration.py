import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Import the POM class


class TestUrbanRoutes:

    driver = webdriver.Chrome()

    @classmethod # Decorator, special marker used to define a method belonging to the class itself
    def setup_class(cls): # cls argument is a class-level method to rfer to the class itself
        cls.driver = webdriver.Chrome() # Class creates a new Chrome browser, stores n the driver variable

    def test_custom_scooter_option(self):

        driver.get('https://cnt-c2b82244-447b-4108-ad53-a14aca3c9e80.containerhub.tripleten-services.com/')

        # Create an instance of the page class
        urban_routes_page = UrbanRoutesPage(self.driver)

        # Step 3: Use POM methods to perform actions on the page
        # Enter "From" and "To" locations.
        urban_routes_page.enter_from_location('East 2nd Street, 601')
        urban_routes_page.enter_to_location('1300 1st St')

        # Select the "Custom" option.
        urban_routes_page.click_custom_option()
        time.sleep(2)  # Adding delay for visibility; optional

        # Click the "Scooter" icon.
        urban_routes_page.click_scooter_icon()
        time.sleep(2)  # Adding delay for visibility; optional

        # Step 4: Call the get_scooter_text() method from the UrbanRoutesPage class to get the text curr
        # currently displayed in the app, where the "Scooter" text should appear.
        # The result is saved in the actual_value variable.
        # Set expected_value to "Scooter", which is the expected
        # text we want to see displayed after selecting the scooter option.
        # Check if expected_value is found within actual_value.
        # If the text "Scooter" is in actual_value, the test passes, and it moves on.
        actual_value = urban_routes_page.get_scooter_text()
        expected_value = "Scooter"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    def test_duration_scooter(self):

        driver.get('https://cnt-c2b82244-447b-4108-ad53-a14aca3c9e80.containerhub.tripleten-services.com/')

        urban_routes_page = UrbanRoutesPage(driver)

        urban_routes_page.enter_from_location('East 2nd Street, 601')
        urban_routes_page.enter_to_location('1300 1st St')

        urban_routes_page.click_custom_option()
        time.sleep(2)
        urban_routes_page.click_scooter_icon()
        time.sleep(2)

        # Verify the Duration text is displayed correctly
        actual_value = urban_routes_page.get_duration_text()
        expected_value = "Duration"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
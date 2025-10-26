import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Import the POM class

driver = webdriver.Chrome()#Driver
driver.maximize_window()#Full Screen Mode

def test_car_brand():
    # Step 1: Open the app - update the URL after starting the server
    driver = webdriver.Chrome()
    driver.get('https://cnt-50928193-76b8-4cf8-bccf-b361223c319d.containerhub.tripleten-services.com/')

    # Create an instance of the page class
    urban_routes_page = UrbanRoutesPage(driver)

    # Step 3: Use POM methods to perform actions on the page
    # Enter "From" and "To" locations.
    urban_routes_page.enter_from_location('East 2nd Street, 601')
    urban_routes_page.enter_to_location('1300 1st St')

    # Select the "Custom" option.
    urban_routes_page.click_custom_option()
    time.sleep(2)  # Adding delay for visibility; optional

    # Click the Drive Button
    urban_routes_page.click_drive_button()
    time.sleep(2)  # Adding delay for visibility; optional

    # Click the Book Button
    urban_routes_page.click_book_button()
    time.sleep(2)

    # Choose the Camping tariff/option
    urban_routes_page.click_camping_option()
    time.sleep(2)

    # Verify Car Make Text "Audi A3 Sedan"
    actual_value = urban_routes_page.get_car_make_text()
    expected_value = "Audi A3 Sedan"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

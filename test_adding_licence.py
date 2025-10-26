import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Import the POM class

driver = webdriver.Chrome()#Driver
driver.maximize_window()#Full Screen Mode

def test_adding_licence():
    # Step 1: Open the app - update the URL after starting the server
    driver = webdriver.Chrome()
    driver.get('https://cnt-7b84c0fe-9d13-45c3-a4f4-5e5dfe69227a.containerhub.tripleten-services.com/')

    # Create an instance of the page class
    urban_routes_page = UrbanRoutesPage(driver)

    # Step 1: Enter the "From" address
    urban_routes_page.enter_from_location('East 2nd Street, 601')

    # Step 2: Enter the "To" address
    urban_routes_page.enter_to_location('1300 1st St')

    # Step 3: Choose "Custom"
    urban_routes_page.click_custom_option()
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 4: Click "Drive"
    urban_routes_page.click_drive_button()
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 5: Click "Book"
    urban_routes_page.click_book_button()
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 6: Choose "Camping"
    urban_routes_page.click_camping_option()
    time.sleep(2)

    # Step 7: Click “Add a driver’s license”
    urban_routes_page.click_add_driver_license()
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 8: Fill out the “First name” field
    urban_routes_page.enter_first_name('Anna')
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 9: Fill out the “Last name” field
    urban_routes_page.enter_last_name('Smith')
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 10: Fill out the “Date of birth” field
    urban_routes_page.enter_date_of_birth('24.04.1889')
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 11: Fill out the “Number” field
    urban_routes_page.enter_number('01 01 123456')
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 12: Click "title" to make the Add button clickable
    urban_routes_page.click_title()
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 13: Click “Add”
    urban_routes_page.click_add_button()
    time.sleep(2)  # Adding delay for visibility; optional

    # Step 14: Check that the licence has been added
    actual_value = urban_routes_page.get_verification_text()
    expected_value = "Thank you!"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    # Verify the Duration text is displayed correctly
    actual_value = urban_routes_page.get_duration_text()
    expected_value = "Duration"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    driver.quit()
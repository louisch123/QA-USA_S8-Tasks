import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage

def test_duration_bike():
    driver = webdriver.Chrome()
    driver.get(' https://cnt-9313f452-b962-4745-9cd6-b4cb0fd4c3bf.containerhub.tripleten-services.com')

    urban_routes_page = UrbanRoutesPage(driver)

    urban_routes_page.enter_from_location('East 2nd Street, 601')
    urban_routes_page.enter_to_location('1300 1st St')

    urban_routes_page.click_custom_option()
    time.sleep(2)
    urban_routes_page.click_bike_icon()
    time.sleep(2)

    # Verify the Duration text is displayed correctly
    actual_value = urban_routes_page.get_duration_text()
    expected_value = "Duration"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    driver.quit()
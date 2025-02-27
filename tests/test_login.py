import time
from pages.login_page import LoginPage

def test_login_valid(browser):
    browser.get("https://www.demoblaze.com/")  # Open website
    login_page = LoginPage(browser)

    # Click on the login button
    browser.find_element("id", "login2").click()
    time.sleep(2)  # Wait for modal to appear

    # Perform login action
    login_page.login("venusmars", "testpassword")

    # Wait and verify login success (checking if Logout button appears)
    time.sleep(2)
    assert browser.find_element("id", "logout2").is_displayed()

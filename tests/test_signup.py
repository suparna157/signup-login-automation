import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.signup_page import SignupPage


def test_signup_validation(browser):
    # Initialize
    browser.get("https://www.demoblaze.com/")
    signup_page = SignupPage(browser)

    # Click sign in link
    signup_page.click_signin_link()

    # First signup attempt
    signup_page.signup("newuser12", "testpassword")

    # Handle alert
    alert_text = signup_page.handle_alert()
    print(f"First signup attempt alert: {alert_text}")

    # Second signup attempt with different username
    signup_page.enter_username("venusmars")
    signup_page.click_signup_button()

    # Handle second alert
    alert_text = signup_page.handle_alert()
    print(f"Second signup attempt alert: {alert_text}")

    # Add assertions based on expected behavior
    assert alert_text is not None, "Expected an alert but none was present"
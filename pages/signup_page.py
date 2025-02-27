from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.signup_input = (By.ID, "sign-username")
        self.password_input = (By.ID, "sign-password")
        self.signup_button = (By.XPATH, "//button[text()='Sign up']")
        self.signin_link = (By.ID, "signin2")

    def click_signin_link(self):
        self.wait.until(EC.element_to_be_clickable(self.signin_link)).click()

    def enter_username(self, username):
        username_field = self.wait.until(EC.element_to_be_clickable(self.signup_input))
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(EC.element_to_be_clickable(self.password_input))
        password_field.clear()
        password_field.send_keys(password)

    def click_signup_button(self):
        self.wait.until(EC.element_to_be_clickable(self.signup_button)).click()

    def signup(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_signup_button()

    def handle_alert(self):
        try:
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            alert_text = alert.text
            alert.accept()
            return alert_text
        except:
            return None


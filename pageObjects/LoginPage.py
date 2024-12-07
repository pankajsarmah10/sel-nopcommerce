from selenium.webdriver.common.by import By

class LoginPage:

    textbox_email = "[name='Email']"
    textbox_password = "[name='Password']"
    button_login = ".login-button"

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_email).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_email).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password).clear()
        self.driver.find_element(By.CSS_SELECTOR, self.textbox_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_login).click()





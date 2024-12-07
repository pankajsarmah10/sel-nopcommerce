from selenium.webdriver.common.by import By

class Dashboard:

    link_logout = "a[href*='logout']"

    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        self.driver.find_element(By.CSS_SELECTOR, self.link_logout).click()
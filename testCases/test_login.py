from pageObjects.LoginPage import LoginPage
import os

from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig


class Test_001_Login:

    base_url = ReadConfig.get_application_url()
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    logger = LogGen.loggen()

    def test_home_page_title(self, setup):
        self.logger.info("*********************** Test_001_Home_Page_Title ***********************")
        self.logger.info("*********************** Verifying Home Page Title ***********************")
        self.driver = setup
        self.driver.get(self.base_url)
        act_title = self.driver.title

        if act_title == 'Your store. Login':
            assert True
            self.driver.close()
            self.driver.quit()
            self.logger.info("*********************** Home Page Title test is passed ***********************")
        else:
            self.driver.save_screenshot(os.path.abspath("Screenshots")+"/test_home_page_title.png")
            self.driver.close()
            self.driver.quit()
            self.logger.error("*********************** Home Page Title test is failed ***********************")
            assert False

    def test_login(self, setup):
        self.logger.info("*********************** Test_002_Login ***********************")
        self.logger.info("*********************** Verifying Login test ***********************")
        self.driver = setup
        self.driver.get(self.base_url)
        login_page = LoginPage(self.driver)
        login_page.set_email(self.email)
        login_page.set_password(self.password)
        login_page.click_login()
        act_title = self.driver.title
        if act_title == 'Dashboard / nopCommerce administration':
            self.driver.close()
            self.driver.quit()
            assert True
            self.logger.info("*********************** Login test is passed ***********************")
        else:
            self.driver.save_screenshot(os.path.abspath("Screenshots")+"/test_home_page_title.png")
            self.driver.close()
            self.driver.quit()
            self.logger.error("*********************** Login test is failed ***********************")
            assert False



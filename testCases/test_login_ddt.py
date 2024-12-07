import time

from pageObjects import DashboardPage
from pageObjects.DashboardPage import Dashboard
from pageObjects.LoginPage import LoginPage
import os

from utilities.custom_logger import LogGen
from utilities.read_properties import ReadConfig
from utilities import ExcelUtils

class Test_002_DDT_Login:

    base_url = ReadConfig.get_application_url()
    path = os.path.abspath('TestData') + '/LoginData.xlsx'
    logger = LogGen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("*********************** Test_002_DDT_Login ***********************")
        self.logger.info("*********************** Verifying Login DDT test ***********************")
        self.driver = setup
        self.driver.get(self.base_url)
        login_page = LoginPage(self.driver)
        dashboard_page = Dashboard(self.driver)
        lst_status = []
        self.rows = ExcelUtils.getRowCount(self.path, 'Sheet1')
        print("No. of rows in the excel: ", self.rows)
        for r in range(2, self.rows + 1):
            self.user = ExcelUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = ExcelUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = ExcelUtils.readData(self.path, 'Sheet1', r, 3)
            login_page.set_email(self.user)
            login_page.set_password(self.password)
            login_page.click_login()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = 'Dashboard / nopCommerce administration'

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Passed ***")
                    dashboard_page.click_logout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*** Failed ***")
                    dashboard_page.click_logout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Failed ***")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*** Passed ***")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT Test is passed.....")
            self.driver.close()
            self.driver.quit()
            assert True
        else:
            self.logger.error("Login DDT Test is failed.....")
            self.driver.close()
            self.driver.quit()
            assert False
        self.logger.info("*********************** End of Login DDT test ***********************")
        self.logger.info("*********************** Completed Test_002_DDT_Login ***********************")

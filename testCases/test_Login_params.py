import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException as Ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import loginpage
from utilites.readproperties import Readconfig
from utilites.Logger import LogGenerator


class Test_Login_Params:
    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    @pytest.mark.regression
    def test_login_params_004(self, setup, getDataforlogin):
        self.driver = setup
        self.log.info("test_login_params_004 is started")
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Go to this url-->" + self.Url)
        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName(getDataforlogin[0])
        self.log.info("Entering username-->" + getDataforlogin[0])
        self.lp.Enter_Password(getDataforlogin[1])
        self.log.info("Entering password-->" + getDataforlogin[1])
        self.lp.Click_Login()
        self.log.info("Click on login button")
        if self.lp.Login_Status() == True:
            if getDataforlogin[2] == "Pass":
                self.driver.save_screenshot(
                    "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\OrangeHrm\\ScreenShots\\test_login_002-pass.png")
                self.lp.Click_MenuButton()
                self.log.info("Click on Menu button")
                self.lp.Click_Logout()
                self.log.info("Click on logout button")
                self.log.info("test_login_002 is Passed")
                assert True
            else:
                self.log.info("test_login_002 is Failed")
                self.driver.save_screenshot(
                    "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\OrangeHrm\\ScreenShots\\test_login_002-fail.png")
                assert False
        else:
            if getDataforlogin[2] == "Fail":
                assert True
            else:
                self.log.info("test_login_002 is Failed")
                self.driver.save_screenshot(
                    "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\OrangeHrm\\ScreenShots\\test_login_002-fail.png")
                assert False

        self.driver.close()
        self.log.info("test_login_002 is Completed")

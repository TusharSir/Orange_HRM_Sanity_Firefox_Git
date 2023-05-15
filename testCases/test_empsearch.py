import time
import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException as Ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from pageObjects.AddEmp_Page import AddEmployee
from pageObjects.EmployeeSearchPage import EmployeeSearch
from pageObjects.LoginPage import loginpage
from utilites.Logger import LogGenerator
from utilites.readproperties import Readconfig


class Test_Search_Emp:
    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    def test_searchEmp_005(self, setup):
        self.log.info("test_searchEmp_005 is started")
        self.driver = setup
        self.log.info("Opening Browser")
        self.driver.get(self.Url)
        self.log.info("Going to Url-->" + self.Url)
        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName(self.username)
        self.log.info("Entering UserName-->" + self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Entering password-->" + self.password)
        self.lp.Click_Login()
        self.log.info("Click On login")
        self.ae = AddEmployee(self.driver)
        self.ae.Click_PIM()
        self.log.info("Click On PIM")
        self.es = EmployeeSearch(self.driver)
        time.sleep(3)
        self.es.Enter_EmpName("David")
        self.log.info("Entering Emp Name")
        time.sleep(2)
        self.es.Click_SearchButton()
        self.log.info("Clicking on search Button")
        time.sleep(2)
        print(self.es.Search_Result())
        if self.es.Search_Result() ==True:
            self.log.info("Search Found")
            self.log.info("test_searchEmp_005 is Passed")
            self.lp.Click_MenuButton()
            self.log.info("Click on MenuButton")
            self.lp.Click_Logout()
            self.log.info("Click on Logout Button")
            assert True
            self.log.info("test_searchEmp_005 is Passed")
        else:
            self.log.info("No Search Found")
            self.lp.Click_MenuButton()
            self.log.info("Click on MenuButton")
            self.lp.Click_Logout()
            self.log.info("Click on Logout Button")
            self.log.info("test_searchEmp_005 is Failed")
            assert False
        self.driver.close()


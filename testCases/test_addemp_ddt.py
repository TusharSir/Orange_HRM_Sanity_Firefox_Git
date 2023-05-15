import time

import pytest

from pageObjects.AddEmp_Page import AddEmployee
from pageObjects.LoginPage import loginpage
from utilites import XLutils
from utilites.Logger import LogGenerator
from utilites.readproperties import Readconfig


class Test_Add_Emp_DDT:
    Url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()
    path = "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\OrangeHrm\\testCases\\TestData\\EmployeeList.xlsx"

    @pytest.mark.regression
    def test_addEmp_ddt_005(self, setup):
        self.log.info("test_addEmp_ddt_005 is started")
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
        self.rows = XLutils.getrowCount(self.path, 'Sheet1')
        print("Number of rows are --->", self.rows)
        self.ae.Click_PIM()
        self.log.info("Click On PIM")
        self.ae.Click_Add()
        self.log.info("Click On Add")
        status_list= []
        for r in range(2, self.rows+1):
            self.FirstName = XLutils.readData(self.path, 'Sheet1',r, 2)
            self.MiddleName = XLutils.readData(self.path, 'Sheet1', r, 3)
            self.LastName = XLutils.readData(self.path, 'Sheet1', r, 4)
            #time.sleep(2)
            self.ae.Enter_FirstName(self.FirstName)
            self.log.info("Entering FirstName-->" + self.FirstName)
            self.ae.Enter_MiddleName(self.MiddleName)
            self.log.info("Entering MiddleName-->" + self.MiddleName)
            self.ae.Enter_LastName(self.LastName)
            self.log.info("Entering LastName--> "+ self.LastName)
            time.sleep(2)
            self.ae.Click_Save()
            self.log.info("Click on Save")
            if self.ae.Add_Employee_stuats() == True:
                self.ae.Click_AddEmployee()
                # time.sleep(2)
                status_list.append("Pass")
                XLutils.writeData(self.path, 'Sheet1', r, 5,"Pass")
                self.driver.save_screenshot(
                    "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\OrangeHrm\\ScreenShots\\test_addEmp_003-pass.png")

            else:
                status_list.append("Fail")
                XLutils.writeData(self.path, 'Sheet1', r, 5, "Fail")
                self.driver.save_screenshot(
                    "D:\\Credence Class Notes\\CredenceBatches\\CredenceBatch#13\\OrangeHrm\\ScreenShots\\test_addEmp_003-fail.png")


        print(status_list)

        time.sleep(2)
        self.lp.Click_MenuButton()
        self.log.info("Click on MenuButton")
        self.lp.Click_Logout()
        self.log.info("Click on Logout Button")
        self.driver.close()
        if "Fail" not in status_list:
            self.log.info("test_addEmp_ddt_005 is Passed")
            assert True
        else:
            self.log.info("test_addEmp_ddt_005 is Failed")
            assert False
        self.log.info("test_addEmp_ddt_005 is Completed")



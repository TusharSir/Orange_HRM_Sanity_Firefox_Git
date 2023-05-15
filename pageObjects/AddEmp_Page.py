from selenium.webdriver.common.by import By

from selenium.common import NoSuchElementException as Ec


class AddEmployee:
    Click_PIM_XPATH = (By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space("
                                 ")='PIM']")
    Click_Add_Button_XPATH = (By.XPATH, "//i[@class='oxd-icon bi-plus oxd-button-icon']")
    Text_FirstName_XPATH = (By.XPATH, "//input[@placeholder='First Name']")
    Text_MiddleName_XPATH = (By.XPATH, "//input[@placeholder='Middle Name']")
    Text_LastName_XPATH = (By.XPATH, "//input[@placeholder='Last Name']")
    Click_Save_Button = (By.XPATH, "//button[@type='submit']")
    PersonalDetails_Tab_XPATH = (By.XPATH, "//h6[normalize-space()='Personal Details']")
    Click_Add_Emp_XPATH = (By.XPATH, "//a[normalize-space()='Add Employee']")

    def __init__(self, driver):
        self.driver = driver

    def Click_PIM(self):
        self.driver.find_element(*AddEmployee.Click_PIM_XPATH).click()

    def Click_Add(self):
        self.driver.find_element(*AddEmployee.Click_Add_Button_XPATH).click()

    def Enter_FirstName(self, firstname):
        self.driver.find_element(*AddEmployee.Text_FirstName_XPATH).send_keys(firstname)

    def Enter_MiddleName(self, middlename):
        self.driver.find_element(*AddEmployee.Text_MiddleName_XPATH).send_keys(middlename)

    def Enter_LastName(self, lastname):
        self.driver.find_element(*AddEmployee.Text_LastName_XPATH).send_keys(lastname)

    def Click_Save(self):
        self.driver.find_element(*AddEmployee.Click_Save_Button).click()

    def Click_AddEmployee(self):
        self.driver.find_element(*AddEmployee.Click_Add_Emp_XPATH).click()

    def Add_Employee_stuats(self):
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element(*AddEmployee.PersonalDetails_Tab_XPATH)
            return True

        except Ec:
            return False

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EmployeeSearch:
    Text_EmpName_XPATH = (By.XPATH, "//input[@xpath='1']")

        # (By.XPATH,
        #                   "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]")
    Click_Search_XPATH = (By.XPATH, "//button[@type='submit']")
    Search_Result_CSS = (By.CSS_SELECTOR,
                         "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1)")

    def __init__(self, driver):
        self.driver = driver

    def Enter_EmpName(self, empname):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located(((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/input[1]"))))
        self.driver.find_element(*EmployeeSearch.Text_EmpName_XPATH).send_keys(empname)

    def Click_SearchButton(self):
        self.driver.find_element(*EmployeeSearch.Click_Search_XPATH).click()

    def Search_Result(self):
        search = self.driver.find_elements(*EmployeeSearch.Search_Result_CSS)
        search_len = len(search)
        if search_len == 0:
            return False
        elif search_len == 1:
            print(self.driver.find_element(*EmployeeSearch.Search_Result_CSS).text)
            return True

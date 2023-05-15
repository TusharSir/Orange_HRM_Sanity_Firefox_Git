import pytest
from selenium import webdriver
from selenium.webdriver.chrome import webdriver
from selenium import webdriver


# In pytest, hook functions are functions that can be used to extend or
# modify the behavior of pytest. They are called automatically by pytest at
# specific times during the test run.

# The pytest_configure function is a hook function in pytest that is called once the
# configuration object has been created and all plugins and initial conftest files have been loaded.

# The pytest_addoption function is a hook function in pytest that is used to add custom command-line options to the
# pytest command. It takes a single argument, parser, which is an instance of the argparse.ArgumentParser class.

def pytest_addoption(parser):
    parser.addoption("--browser")


# Define the browser fixture function with a single argument, request.
# Within the browser function, use the request.config.getoption() method to get the value
# of the --browser option passed to pytest on the command line.
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    elif browser == 'edge':
        print("Launching Edge Browser")
        driver = webdriver.Edge()
    else:
        print("Headless mode")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("headless")
        #driver = webdriver.Firefox()
        driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


# The pytest_metadata function is a hook function in pytest that allows you to
# add custom metadata to the test report. This metadata can be used to provide
# additional information about the test run, such as the environment, the test data,
# or any other relevant information.

def pytest_metadata(metadata):
    # To Add
    metadata["Environment"] = "Test"
    metadata['Project Name'] = 'OrangHRM'
    metadata['Module Name'] = 'Employee'
    metadata['Tester'] = 'Credence'
    # Remove
    metadata.pop("Packages", None)
    metadata.pop("Plugins", None)


@pytest.fixture(params=[
    ("Admin", "admin123", "Pass"),
    ("Admin1", "admin123", "Fail"),
    ("Admin", "admin1231", "Fail"),
    ("Admin1", "admin1231", "Fail")
])
def getDataforlogin(request):
    return request.param

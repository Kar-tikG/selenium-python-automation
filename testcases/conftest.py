import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def setup(request, browser, url):
    if browser=="chrome":
        driver = webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    elif browser=="edge":
        driver=webdriver.Edge()
    driver.get(url)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--url")

@pytest.fixture(scope='class', autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope='class', autouse=True)
def url(request):
    return request.config.getoption("--url")

# @pytest.fixture(scope='class')
# def setup(request):
#     driver = webdriver.Chrome()
#     driver.get("https://www.yatra.com/")
#     driver.maximize_window()
#     request.cls.driver=driver
#     yield
#     driver.close()
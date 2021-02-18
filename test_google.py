import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture()
def test_setup():
    global driver
    # @pytest.mark.repeat(3)
    driver = webdriver.Chrome("venv/Scripts/chromedriver.exe")
    driver.maximize_window()
    yield
    driver.close()


def test_google(test_setup):
    # browser = webdriver.Chrome("C:\\selenium drivers\\chromedriver_win32\\chromedriver.exe")
    driver.get('http://google.com')

    try:
        driver.find_element_by_xpath('//*[@id="hpl0go"]')
        print("Element exist")
    except NoSuchElementException:
        print("Element does not exist")

    x = driver.title
    assert x == "Google"


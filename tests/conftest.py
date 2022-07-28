import pytest

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=800,600')
    return options

@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    #s = Service('C:\\Users\\Admin\\Desktop\\GoogleTranslate\\chromedriver_win32\\chromedriver.exe')
    #driver = webdriver.Chrome(service=s)
    return driver

@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://translate.google.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    time.sleep(5)
    yield driver
    driver.quit()
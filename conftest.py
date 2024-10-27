import random
import string
import pytest
import requests
from allure_commons import fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import data
import links
from data import email
from locators.login_locators import LoginLocators
from locators.main_page_locators import MainPageLocators
from pages.profile_page import Profile


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser_name = request.param
    driver = None
    if browser_name == 'chrome':
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.set_window_size(1920, 1080)
    elif browser_name == 'firefox':
        options = webdriver.FirefoxOptions()
        options.binary_location = "/opt/firefox/firefox"
        driver = webdriver.Firefox(service=FirefoxService(executable_path=GeckoDriverManager().install()), options=options)
        driver.set_window_size(1920, 1080)
        # driver.implicitly_wait(10)
    else:
        ValueError("Can't create instatnce for this browser param")
    yield driver
    driver.quit()

@pytest.fixture()
def setup():
    letters = string.ascii_lowercase
    email = f"{(''.join(random.choice(letters) for _ in range(8))) + '@yandex.ru'}"
    password = ''.join(random.choice(letters) for _ in range(8))
    name = ''.join(random.choice(letters) for _ in range(8))
    response = requests.post(f"{links.link_main}/api/auth/register", json={
        "email": email,
        "password": password,
        "name": name
    })
    yield {'email': response.json()['user']['email'],
            'name': response.json()['user']['name'],
            'password': password,
            'accessToken': response.json()['accessToken']
            }
    requests.delete(f"{links.link_main}/api/auth/user")

@pytest.fixture()
def login_to_profile(driver, setup):
    profile = Profile(driver)
    profile.get_url(links.link_login)
    profile.set_input(LoginLocators.MAIL_INNER, setup['email'])
    profile.set_input(LoginLocators.PASSWORD_INNER, setup['password'])
    profile.click_to_button(LoginLocators.BUTTON_INNER)
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(links.link_main))
    profile.click_to_button(MainPageLocators.PROFILE)
    WebDriverWait(driver, 10).until(expected_conditions.url_to_be(links.link_profile))
    return profile

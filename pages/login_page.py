import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import links
from locators.login_locators import LoginLocators
from pages.base_page import BasePage


class Login(BasePage):


    @allure.title("login_to_profile")
    def login_to_profile(self, login_email, login_password):
        self.get_url(links.link_login)
        self.set_input(LoginLocators.MAIL_INNER, login_email)
        self.set_input(LoginLocators.PASSWORD_INNER, login_password)
        self.click_to_button(LoginLocators.BUTTON_INNER)
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(links.link_main))

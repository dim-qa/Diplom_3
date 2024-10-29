import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
import links
from locators.forgor_password_locators import ForgotPasswordLocators
from pages.base_page import BasePage

class ResetPassword(BasePage):

    @allure.step("клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def click_to_inner_mail(self):

        self.get_url(links.LINK_RESET_PASSWORD)
        self.click_to_button(ForgotPasswordLocators.RECOVERY_BUTTON)
        WebDriverWait(self.driver, self.wait_time).until(expected_conditions.url_to_be(links.LINK_RESET_PASSWORD))

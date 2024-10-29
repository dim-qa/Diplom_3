import allure

import data
import links
from locators.forgor_password_locators import ForgotPasswordLocators
from locators.login_locators import LoginLocators
from locators.reset_password_locators import ResetPasswordLocators
from pages.base_page import BasePage

class ForgotPassword(BasePage):

    @allure.step("переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def click_to_recovery_button(self):
        self.get_url(links.LINK_LOGIN)
        self.click_to_button(LoginLocators.RECOVERY_LINK)

    @allure.step("ввод почты и клик по кнопке «Восстановить»")
    def inner_recovery_mail(self):
        self.get_url(links.LINK_FORGOT_PASSWORD)
        self.set_input(ForgotPasswordLocators.INNER_MAIL, data.email)
        self.click_to_button(ForgotPasswordLocators.RECOVERY_BUTTON)
        self.wait_an_element(ResetPasswordLocators.INNER_MAIL)

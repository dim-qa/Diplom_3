import allure
from pages.base_page import BasePage

class ForgotPassword(BasePage):

    @allure.title("click_to_recovery_button")
    def click_to_recovery_button(self, locator):
        self.wait_an_element(locator)
        self.click_to_button(locator)

    @allure.title("inner_recovery_mail")
    def inner_recovery_mail(self, locator, mail):
        self.set_input(locator, mail)

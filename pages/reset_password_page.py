import allure
from pages.base_page import BasePage

class ResetPassword(BasePage):

    @allure.title("click_to_inner_mail")
    def click_to_inner_mail(self, locator):
        self.wait_an_element(locator)
        self.click_to_button(locator)

import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
import links
from locators.profile_locators import ProfileLocators
from pages.base_page import BasePage


class Profile(BasePage):


    @allure.step("переход в раздел «История заказов»")
    def open_order_history(self):
        WebDriverWait(self.driver, self.wait_time).until(expected_conditions.url_to_be(links.LINK_PROFILE))
        self.click_to_button(ProfileLocators.ORDER_HISTORY)
        WebDriverWait(self.driver, self.wait_time).until(expected_conditions.url_to_be(links.ORDER_HISTORY))

    @allure.step("выход из аккаунта")
    def exit_profile(self):
        WebDriverWait(self.driver, self.wait_time).until(expected_conditions.url_to_be(links.LINK_PROFILE))
        self.click_to_button(ProfileLocators.EXIT_BUTTON)
        WebDriverWait(self.driver, self.wait_time).until(expected_conditions.url_to_be(links.LINK_LOGIN))

import allure
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import links
from locators.profile_locators import ProfileLocators
from pages.base_page import BasePage


class Profile(BasePage):


    @allure.title("open_order_history")
    def open_order_history(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(links.link_profile))
        element = self.driver.find_element(*ProfileLocators.ORDER_HISTORY)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(links.order_history))

    @allure.title("exit_profile")
    def exit_profile(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(links.link_profile))
        element = self.driver.find_element(*ProfileLocators.EXIT_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(links.link_login))

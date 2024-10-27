import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import links
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.title("switch_to_constructor")
    def switch_to_constructor(self):
        self.get_url(links.link_login)
        element = self.driver.find_element(*MainPageLocators.CONSTRUCTOR)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.title("order_list")
    def order_list(self):
        self.get_url(links.link_main)
        element = self.driver.find_element(*MainPageLocators.ORDER_LIST)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.title("pop_up_window_with_details")
    def pop_up_window_with_details(self):
        self.get_url(links.link_main)
        self.click_to_button(MainPageLocators.R2_D3)

    @allure.title("clouse_pop_up")
    def clouse_pop_up(self):
        self.get_url(links.link_main)
        self.click_to_button(MainPageLocators.R2_D3)
        element = self.driver.find_element(*MainPageLocators.EXIT_POP_UP)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.title("count")
    def count(self):
        self.get_url(links.link_main)
        start_count = self.driver.find_element(*MainPageLocators.COUNT).text
        self.drag_and_drop(MainPageLocators.R2_D3, MainPageLocators.SPAN_DROP)
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*MainPageLocators.COUNT).text != '0')
        result_count = self.driver.find_element(*MainPageLocators.COUNT).text
        return start_count, result_count

    @allure.title("get_order")
    def get_order(self):
        self.get_url(links.link_main)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.R2_D3_IMG))
        self.drag_and_drop(MainPageLocators.R2_D3_IMG, MainPageLocators.SPAN_DROP)
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*MainPageLocators.COUNT).text != '0')
        self.click_to_button(MainPageLocators.ORDER_BUTTON)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_READY)
        )

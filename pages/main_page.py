import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import data
import links
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("переход по клику на «Конструктор»")
    def switch_to_constructor(self):
        self.get_url(links.LINK_LOGIN)
        self.click_to_button(MainPageLocators.CONSTRUCTOR)

    @allure.step("переход по клику на «Лента заказов»")
    def order_list(self):
        self.get_url(links.LINK_MAIN)
        self.click_to_button(MainPageLocators.ORDER_LIST)

    @allure.step("если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def pop_up_window_with_details(self):
        self.get_url(links.LINK_MAIN)
        self.click_to_button(MainPageLocators.R2_D3)

    @allure.step("всплывающее окно закрывается кликом по крестику")
    def clouse_pop_up(self):
        self.get_url(links.LINK_MAIN)
        self.click_to_button(MainPageLocators.R2_D3)
        self.click_to_button(MainPageLocators.EXIT_POP_UP)

    @allure.step("при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def count(self):
        self.get_url(links.LINK_MAIN)
        start_count = self.driver.find_element(*MainPageLocators.COUNT).text
        self.drag_and_drop(MainPageLocators.R2_D3, MainPageLocators.SPAN_DROP)
        WebDriverWait(self.driver, self.wait_time).until(
            lambda driver: driver.find_element(*MainPageLocators.COUNT).text != '0')
        result_count = self.driver.find_element(*MainPageLocators.COUNT).text
        return start_count, result_count

    @allure.step("залогиненный пользователь может оформить заказ")
    def get_order(self):
        self.get_url(links.LINK_MAIN)
        WebDriverWait(self.driver, self.wait_time).until(expected_conditions.visibility_of_element_located(MainPageLocators.R2_D3_IMG))
        self.drag_and_drop(MainPageLocators.R2_D3_IMG, MainPageLocators.SPAN_DROP)
        WebDriverWait(self.driver, self.wait_time).until(
            lambda driver: driver.find_element(*MainPageLocators.COUNT).text != '0')
        self.click_to_button(MainPageLocators.ORDER_BUTTON)
        WebDriverWait(self.driver, self.wait_time).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.ORDER_READY)
        )

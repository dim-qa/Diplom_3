from unittest import expectedFailure
import allure
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from setuptools.archive_util import extraction_drivers
import links
import time
from locators.feed_locators import FeedLocators
from locators.login_locators import LoginLocators
from locators.main_page_locators import MainPageLocators
from locators.profile_locators import ProfileLocators
from pages.base_page import BasePage


class FeedPage(BasePage):


    @allure.title("open_pop_up_details_of_order")
    def open_pop_up_details_of_order(self):
        self.get_url(links.link_feeds)
        self.click_to_button(FeedLocators.ORDERS)

    @allure.title("order_history_correct_on_order_list")
    def order_history_correct_on_order_list(self):
        self.get_url(links.link_main)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(MainPageLocators.R2_D3_IMG))
        self.drag_and_drop(MainPageLocators.R2_D3_IMG, MainPageLocators.SPAN_DROP)
        self.click_to_button(MainPageLocators.ORDER_BUTTON)
        self.waiting_an_element()
        number = self.wait_an_element(MainPageLocators.NUMBER_ORDER).text
        element = self.driver.find_element(*MainPageLocators.EXIT_ORDER_POP_UP)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(MainPageLocators.PROFILE))
        element = self.driver.find_element(*MainPageLocators.PROFILE)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(ProfileLocators.ORDER_HISTORY))
        element = self.driver.find_element(*ProfileLocators.ORDER_HISTORY)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(ProfileLocators.ORDER_NUMBER_PROFILE))
        text = self.driver.find_element(*ProfileLocators.ORDER_NUMBER_PROFILE).text
        return number, text

    @allure.title("count_sum")
    def count_sum(self):
        self.get_url(links.link_main)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.R2_D3_IMG))
        element = self.driver.find_element(*MainPageLocators.ORDER_LIST)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(FeedLocators.ORDERS))
        count_sum = self.wait_an_element(FeedLocators.COUNT_SUM).text
        element = self.driver.find_element(*MainPageLocators.CONSTRUCTOR)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.R2_D3_IMG))
        self.drag_and_drop(MainPageLocators.R2_D3_IMG, MainPageLocators.SPAN_DROP)
        self.click_to_button(MainPageLocators.ORDER_BUTTON)
        element = self.driver.find_element(*MainPageLocators.EXIT_ORDER_POP_UP)
        self.driver.execute_script("arguments[0].click();", element)
        element = self.driver.find_element(*MainPageLocators.ORDER_LIST)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(FeedLocators.COUNT_SUM))
        text = self.driver.find_element(*FeedLocators.COUNT_SUM).text
        return count_sum, text

    @allure.title("count_today")
    def count_today(self):
        self.get_url(links.link_main)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.R2_D3_IMG))
        element = self.driver.find_element(*MainPageLocators.ORDER_LIST)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(FeedLocators.ORDERS))
        count_sum = self.wait_an_element(FeedLocators.COUNT_TODAY).text
        element = self.driver.find_element(*MainPageLocators.CONSTRUCTOR)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.R2_D3_IMG))
        self.drag_and_drop(MainPageLocators.R2_D3_IMG, MainPageLocators.SPAN_DROP)
        self.click_to_button(MainPageLocators.ORDER_BUTTON)
        element = self.driver.find_element(*MainPageLocators.EXIT_ORDER_POP_UP)
        self.driver.execute_script("arguments[0].click();", element)
        element = self.driver.find_element(*MainPageLocators.ORDER_LIST)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(FeedLocators.COUNT_SUM))
        text = self.driver.find_element(*FeedLocators.COUNT_TODAY).text
        return count_sum, text

    @allure.title("in_work")
    def in_work(self):
        self.get_url(links.link_main)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.R2_D3_IMG))
        self.drag_and_drop(MainPageLocators.R2_D3_IMG, MainPageLocators.SPAN_DROP)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.ORDER_BUTTON))
        self.click_to_button(MainPageLocators.ORDER_BUTTON)
        self.waiting_an_element()
        number = self.wait_an_element(MainPageLocators.NUMBER_ORDER).text
        element = self.driver.find_element(*MainPageLocators.EXIT_ORDER_POP_UP)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(MainPageLocators.ORDER_LIST))
        element = self.driver.find_element(*MainPageLocators.ORDER_LIST)
        self.driver.execute_script("arguments[0].click();", element)
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(FeedLocators.IN_WORK))
        text = self.driver.find_element(*FeedLocators.IN_WORK).text
        return number, text




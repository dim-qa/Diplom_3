import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import links
from locators.feed_locators import FeedLocators
from locators.main_page_locators import MainPageLocators
from locators.profile_locators import ProfileLocators
from pages.base_page import BasePage


class FeedPage(BasePage):


    @allure.step("если кликнуть на заказ, откроется всплывающее окно с деталями")
    def open_pop_up_details_of_order(self):
        self.get_url(links.LINK_FEEDS)
        self.driver.find_element(*FeedLocators.ORDERS).click()
        #javascript клик точный, и выдает ошибку, от selenium кликает первый заказ не разбирая

    @allure.step("заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def order_history_correct_on_order_list(self):
        self.get_url(links.LINK_MAIN)
        WebDriverWait(self.driver, self.wait_time).until(expected_conditions.visibility_of_element_located(MainPageLocators.R2_D3_IMG))
        self.drag_and_drop(MainPageLocators.R2_D3_IMG, MainPageLocators.SPAN_DROP)
        self.click_to_button(MainPageLocators.ORDER_BUTTON)
        self.waiting_an_element()
        number = self.wait_an_element(MainPageLocators.NUMBER_ORDER).text
        self.click_to_button(MainPageLocators.EXIT_ORDER_POP_UP)
        WebDriverWait(self.driver, self.wait_time).until(expected_conditions.element_to_be_clickable(MainPageLocators.PROFILE))
        self.click_to_button(MainPageLocators.PROFILE)
        WebDriverWait(self.driver, self.wait_time).until(expected_conditions.element_to_be_clickable(ProfileLocators.ORDER_HISTORY))
        self.click_to_button(ProfileLocators.ORDER_HISTORY)
        WebDriverWait(self.driver, self.wait_time).until(expected_conditions.visibility_of_element_located(ProfileLocators.ORDER_NUMBER_PROFILE))
        text = self.driver.find_element(*ProfileLocators.ORDER_NUMBER_PROFILE).text
        return number, text

    @allure.step("при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def count_sum(self):
        self.get_url(links.LINK_MAIN)
        WebDriverWait(self.driver, self.wait_time).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.R2_D3_IMG))
        self.click_to_button(MainPageLocators.ORDER_LIST)
        WebDriverWait(self.driver, self.wait_time).until(
            expected_conditions.visibility_of_element_located(FeedLocators.ORDERS))
        count_sum = self.wait_an_element(FeedLocators.COUNT_SUM).text
        self.click_to_button(MainPageLocators.CONSTRUCTOR)
        WebDriverWait(self.driver, self.wait_time).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.R2_D3_IMG))
        self.drag_and_drop(MainPageLocators.R2_D3_IMG, MainPageLocators.SPAN_DROP)
        self.click_to_button(MainPageLocators.ORDER_BUTTON)
        self.click_to_button(MainPageLocators.EXIT_ORDER_POP_UP)
        self.click_to_button(MainPageLocators.ORDER_LIST)
        WebDriverWait(self.driver, self.wait_time).until(expected_conditions.element_to_be_clickable(FeedLocators.COUNT_SUM))
        text = self.driver.find_element(*FeedLocators.COUNT_SUM).text
        return count_sum, text

    @allure.step("при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def count_today(self):
        self.get_url(links.LINK_MAIN)
        WebDriverWait(self.driver, self.wait_time).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.R2_D3_IMG))
        self.click_to_button(MainPageLocators.ORDER_LIST)
        WebDriverWait(self.driver, self.wait_time).until(
            expected_conditions.visibility_of_element_located(FeedLocators.ORDERS))
        count_sum = self.wait_an_element(FeedLocators.COUNT_TODAY).text
        self.click_to_button(MainPageLocators.CONSTRUCTOR)
        WebDriverWait(self.driver, self.wait_time).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.R2_D3_IMG))
        self.drag_and_drop(MainPageLocators.R2_D3_IMG, MainPageLocators.SPAN_DROP)
        self.click_to_button(MainPageLocators.ORDER_BUTTON)
        self.click_to_button(MainPageLocators.EXIT_ORDER_POP_UP)
        self.click_to_button(MainPageLocators.ORDER_LIST)
        WebDriverWait(self.driver, self.wait_time).until(expected_conditions.element_to_be_clickable(FeedLocators.COUNT_SUM))
        element = self.wait_an_element(FeedLocators.COUNT_TODAY)
        WebDriverWait(self.driver, self.wait_time).until(lambda driver: element.text != count_sum)
        text = self.driver.find_element(*FeedLocators.COUNT_TODAY).text
        return count_sum, text

    @allure.step("после оформления заказа его номер появляется в разделе В работе")
    def in_work(self):
        self.get_url(links.LINK_MAIN)
        WebDriverWait(self.driver, self.wait_time).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.R2_D3_IMG))
        self.drag_and_drop(MainPageLocators.R2_D3_IMG, MainPageLocators.SPAN_DROP)
        WebDriverWait(self.driver, self.wait_time).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.ORDER_BUTTON))
        self.click_to_button(MainPageLocators.ORDER_BUTTON)
        self.waiting_an_element()
        number = self.wait_an_element(MainPageLocators.NUMBER_ORDER).text
        self.click_to_button(MainPageLocators.EXIT_ORDER_POP_UP)
        WebDriverWait(self.driver, self.wait_time).until(expected_conditions.element_to_be_clickable(MainPageLocators.ORDER_LIST))
        self.click_to_button(MainPageLocators.ORDER_LIST)
        WebDriverWait(self.driver, self.wait_time).until(expected_conditions.element_to_be_clickable(FeedLocators.IN_WORK))
        text = self.driver.find_element(*FeedLocators.IN_WORK).text
        return number, text




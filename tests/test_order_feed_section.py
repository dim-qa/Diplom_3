import allure
import data
from locators.feed_locators import FeedLocators
from pages.feed_page import FeedPage


class TestOrderFeedSection:


    @allure.title("тест, если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_open_pop_up_details_of_order(self, driver):
        feed = FeedPage(driver)
        feed.open_pop_up_details_of_order()
        element = feed.driver.find_element(*FeedLocators.POP_UP).text
        assert element == data.POP_UP_DETAIL

    @allure.title("тест, заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»")
    def test_order_history_correct_on_order_list(self, driver, login_to_profile):
        feed = FeedPage(driver)
        number1, number11 = feed.order_history_correct_on_order_list()
        assert f"#0{number1}" == number11

    @allure.title("тест, при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_count_sum(self, driver, login_to_profile):
        feed = FeedPage(driver)
        number1, number11 = feed.count_sum()
        assert number1 < number11

    @allure.title("тест, при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_count_today(self, driver, login_to_profile):
        feed = FeedPage(driver)
        number1, number11 = feed.count_today()
        assert number1 < number11

    @allure.title("тест, после оформления заказа его номер появляется в разделе В работе")
    def test_in_work(self, driver, login_to_profile):
        feed = FeedPage(driver)
        number1, number11 = feed.in_work()
        assert f"0{number1}" == number11


import allure
import data
import links
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestCheckMainFunc:


    @allure.title("тест перехода по клику на «Конструктор»")
    def test_switch_to_construsctor(self, driver):
        main_page = MainPage(driver)
        main_page.switch_to_constructor()
        assert main_page.url() == links.LINK_MAIN

    @allure.title("тест перехода по клику на «Лента заказов»")
    def test_order_list(self, driver):
        main_page = MainPage(driver)
        main_page.order_list()
        assert main_page.url() == links.LINK_FEED

    @allure.title("тест, если кликнуть на ингредиент, появится всплывающее окно с деталями")
    def test_pop_up_window_with_details(self, driver):
        main_page = MainPage(driver)
        main_page.pop_up_window_with_details()
        element1 = main_page.get_text(MainPageLocators.R2_D3)
        element11 = main_page.get_text(MainPageLocators.R2_D3_POP_UP)
        assert element1 == element11

    @allure.title("тест, всплывающее окно закрывается кликом по крестику")
    def test_clouse_pop_up(self, driver):
        main_page = MainPage(driver)
        main_page.clouse_pop_up()
        elements = main_page.driver.find_elements(*MainPageLocators.EXIT_POP_UP)
        assert len(elements) == 0

    @allure.title("тест, при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента")
    def test_count(self, driver):
        main_page = MainPage(driver)
        count1, count11 = main_page.count()
        assert count1 != count11

    @allure.title("тест, залогиненный пользователь может оформить заказ")
    def test_get_order(self, driver, login_to_profile):
        main_page = MainPage(driver)
        main_page.get_order()
        element = main_page.driver.find_element(*MainPageLocators.ORDER_READY).text
        assert element == data.ORDER_READY_TEXT


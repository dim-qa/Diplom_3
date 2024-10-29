import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import links
from locators.main_page_locators import MainPageLocators
from pages.login_page import Login


class TestPersonalAccount:


    @allure.title("тест перехода по клику на «Личный кабинет»")
    def test_personal_account(self, driver, setup):
        login = Login(driver)
        login.login_to_profile(setup['email'], setup['password'])
        login.click_to_button(MainPageLocators.PROFILE)
        WebDriverWait(driver, data.WAIT_TIME).until(expected_conditions.url_to_be(links.LINK_PROFILE))
        assert login.url() == links.LINK_PROFILE

    @allure.title("тест перехода в раздел «История заказов»")
    def test_switch_order_history(self, driver, login_to_profile):
        login_to_profile.open_order_history()
        assert login_to_profile.url() == links.ORDER_HISTORY

    @allure.title("тест выхода из аккаунта")
    def test_exit_profile(self, driver, login_to_profile):
        login_to_profile.exit_profile()
        assert login_to_profile.url() == links.LINK_LOGIN

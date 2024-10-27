import time
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import links
from locators.feed_locators import FeedLocators
from locators.forgor_password_locators import ForgotPasswordLocators
from locators.login_locators import LoginLocators
from locators.main_page_locators import MainPageLocators
from locators.reset_password_locators import ResetPasswordLocators
from pages.feed_page import FeedPage
from pages.forgot_password_page import ForgotPassword
from pages.login_page import Login
from pages.main_page import MainPage
from pages.reset_password_page import ResetPassword


class TestRecovery:


    @allure.step("test_click_recovery_link")
    def test_click_recovery_link(self, driver):
        login = Login(driver)
        login.get_url(links.link_login)
        login.click_to_button(LoginLocators.RECOVERY_LINK)
        assert login.url() == links.link_forgot_password

    @allure.step("test_inner_mail_press_recovery")
    def test_inner_mail_press_recovery(self, driver):
        forgot_password = ForgotPassword(driver)
        forgot_password.get_url(links.link_forgot_password)
        forgot_password.inner_recovery_mail(ForgotPasswordLocators.INNER_MAIL, data.email)
        forgot_password.click_to_recovery_button(ForgotPasswordLocators.RECOVERY_BUTTON)
        forgot_password.wait_an_element(ResetPasswordLocators.INNER_MAIL)
        assert forgot_password.url() == links.link_reset_password

    @allure.step("test_active_input")
    def test_active_input(self, driver):
        reset_password =ResetPassword(driver)
        reset_password.get_url(links.link_reset_password)
        reset_password.click_to_button(ForgotPasswordLocators.RECOVERY_BUTTON)
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(links.link_reset_password))
        element = reset_password.driver.find_element(*ResetPasswordLocators.INNER_MAIL)
        initial_class = element.get_attribute('type')
        element = reset_password.driver.find_element(*ResetPasswordLocators.EYE)
        driver.execute_script("arguments[0].click();", element)
        WebDriverWait(driver, 10).until(lambda d: element.get_attribute('type') != initial_class)
        element = reset_password.driver.find_element(*ResetPasswordLocators.INNER_MAIL)
        arr = element.get_attribute('type')
        assert initial_class != arr

    @allure.step("test_personal_account")
    def test_personal_account(self, driver, setup):
        login = Login(driver)
        login.login_to_profile(setup['email'], setup['password'])
        login.click_to_button(MainPageLocators.PROFILE)
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(links.link_profile))
        assert login.url() == links.link_profile

    @allure.step("test_switch_order_history")
    def test_switch_order_history(self, driver, login_to_profile):
        login_to_profile.open_order_history()
        assert login_to_profile.url() == links.order_history

    @allure.step("test_exit_profile")
    def test_exit_profile(self, driver, login_to_profile):
        login_to_profile.exit_profile()
        assert login_to_profile.url() == links.link_login

    @allure.step("test_switch_to_construsctor")
    def test_switch_to_construsctor(self, driver):
        main_page = MainPage(driver)
        main_page.switch_to_constructor()
        assert main_page.url() == links.link_main

    @allure.step("test_order_list")
    def test_order_list(self, driver):
        main_page = MainPage(driver)
        main_page.order_list()
        assert main_page.url() == links.link_feeds

    @allure.step("test_pop_up_window_with_details")
    def test_pop_up_window_with_details(self, driver):
        main_page = MainPage(driver)
        main_page.pop_up_window_with_details()
        element1 = main_page.get_text(MainPageLocators.R2_D3)
        element11 = main_page.get_text(MainPageLocators.R2_D3_POP_UP)
        assert element1 == element11

    @allure.step("test_clouse_pop_up")
    def test_clouse_pop_up(self, driver):
        main_page = MainPage(driver)
        main_page.clouse_pop_up()
        elements = main_page.driver.find_elements(*MainPageLocators.EXIT_POP_UP)
        assert len(elements) == 0

    @allure.step("test_count")
    def test_count(self, driver):
        main_page = MainPage(driver)
        count1, count11 = main_page.count()
        assert count1 != count11

    @allure.step("test_get_order")
    def test_get_order(self, driver, login_to_profile):
        main_page = MainPage(driver)
        main_page.get_order()
        element = main_page.driver.find_element(*MainPageLocators.ORDER_READY).text
        time.sleep(3)
        assert element == data.ORDER_READY_TEXT

    @allure.step("test_open_pop_up_details_of_order")
    def test_open_pop_up_details_of_order(self, driver):
        feed = FeedPage(driver)
        feed.open_pop_up_details_of_order()
        element = feed.driver.find_element(*FeedLocators.POP_UP).text
        assert element==data.POP_UP_DETAIL

    @allure.step("test_order_history_correct_on_order_list")
    def test_order_history_correct_on_order_list(self, driver, login_to_profile):
        feed = FeedPage(driver)
        number1, number11 = feed.order_history_correct_on_order_list()
        assert f"#0{number1}" == number11

    @allure.step("test_count_sum")
    def test_count_sum(self, driver, login_to_profile):
        feed = FeedPage(driver)
        number1, number11 = feed.count_sum()
        assert number1 < number11

    @allure.step("test_count_today")
    def test_count_today(self, driver, login_to_profile):
        feed = FeedPage(driver)
        number1, number11 = feed.count_today()
        assert number1 < number11

    @allure.step("test_in_work")
    def test_in_work(self, driver, login_to_profile):
        feed =FeedPage(driver)
        number1, number11 = feed.in_work()
        assert f"0{number1}" == number11

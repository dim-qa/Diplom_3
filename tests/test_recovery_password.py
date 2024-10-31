import allure
from selenium.webdriver.support.wait import WebDriverWait
import data
import links
from locators.reset_password_locators import ResetPasswordLocators
from pages.forgot_password_page import ForgotPassword
from pages.reset_password_page import ResetPassword


class TestRecoveryPassword:


    @allure.title("тест перехода на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_click_recovery_link(self, driver):
        forgot_password = ForgotPassword(driver)
        forgot_password.click_to_recovery_button()
        assert forgot_password.url() == links.LINK_FORGOT_PASSWORD

    @allure.title("тест ввода почты и клик по кнопке «Восстановить»")
    def test_inner_mail_press_recovery(self, driver):
        forgot_password = ForgotPassword(driver)
        forgot_password.inner_recovery_mail()
        assert forgot_password.url() == links.LINK_RESET_PASSWORD

    @allure.title("тест клика по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_active_input(self, driver):
        reset_password = ResetPassword(driver)
        reset_password.click_to_inner_mail()
        element = reset_password.driver.find_element(*ResetPasswordLocators.INNER_MAIL)
        initial_class = element.get_attribute('type')
        reset_password.click_to_button(ResetPasswordLocators.EYE)
        WebDriverWait(driver, data.WAIT_TIME).until(lambda d: element.get_attribute('type') != initial_class)
        element = reset_password.driver.find_element(*ResetPasswordLocators.INNER_MAIL)
        arr = element.get_attribute('type')
        assert initial_class != arr


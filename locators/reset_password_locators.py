from selenium.webdriver.common.by import By

class ResetPasswordLocators:


    INNER_MAIL = By.XPATH, ".//*[@name='Введите новый пароль']"
    EYE = By.XPATH, ".//*[@class='input__icon input__icon-action']"
    ACTIVE_INNER = By.XPATH, ".//*[@name='Введите новый пароль']/parent::div"

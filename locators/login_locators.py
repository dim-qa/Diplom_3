from selenium.webdriver.common.by import By

class LoginLocators:


    RECOVERY_LINK   = By.XPATH, ".//*[starts-with(@class, 'Auth') and text()='Восстановить пароль']"
    MAIL_INNER = By.XPATH, ".//*[@class = 'text input__textfield text_type_main-default' and @name = 'name']"
    PASSWORD_INNER = By.XPATH, ".//*[@class = 'text input__textfield text_type_main-default' and @name = 'Пароль']"
    BUTTON_INNER = By.XPATH, ".//button[contains(text(),'Войти')]"

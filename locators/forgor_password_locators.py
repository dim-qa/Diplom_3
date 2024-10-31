from selenium.webdriver.common.by import By

class ForgotPasswordLocators:

    INNER_MAIL = By.XPATH, ".//input"
    RECOVERY_BUTTON = By.XPATH, ".//*[text()='Восстановить']"

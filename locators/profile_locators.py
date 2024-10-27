from selenium.webdriver.common.by import By


class ProfileLocators:

    ORDER_HISTORY = By.XPATH, ".//a[contains(@class,'Account_link__2ETsJ') and @href = '/account/order-history']"
    EXIT_BUTTON = By.XPATH, ".//button[contains(@class,'Account_button__14Yp3') and text()='Выход']"
    ORDER_NUMBER_PROFILE = By.XPATH, ".//*[@class= 'text text_type_digits-default']"

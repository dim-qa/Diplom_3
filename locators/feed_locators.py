from selenium.webdriver.common.by import By


class FeedLocators:


    TEXT_ORDER_LIST = By.XPATH, ".//*[text()= 'Лента заказов']"
    ORDERS = By.XPATH, ".//ul[@class = 'OrderFeed_list__OLh59']/li"
    POP_UP = By.XPATH, ".//*[@class= 'text text_type_main-medium mb-8']"
    COUNT_SUM = By.XPATH, ".//*[text()='Выполнено за все время:']/parent::div/p[starts-with(@class, 'OrderFeed_number__2MbrQ')]"
    COUNT_TODAY = By.XPATH, ".//*[text()='Выполнено за сегодня:']/parent::div/p[starts-with(@class, 'OrderFeed_number__2MbrQ')]"
    IN_WORK = By.XPATH, ".//li[contains(@class, 'text text_type_digits-default mb-2')]/parent::ul[starts-with(@class, 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi')]/li"

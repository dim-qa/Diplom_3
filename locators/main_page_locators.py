from selenium.webdriver.common.by import By


class MainPageLocators:


    PROFILE = By.XPATH, ".//a[contains(@class,'AppHeader_header') and @href = '/account']"
    CONSTRUCTOR = By.XPATH, ".//p[contains(@class,'AppHeader') and text()='Конструктор']"
    ORDER_LIST = By.XPATH, ".//p[contains(@class,'AppHeader_header') and text()='Лента Заказов']"
    R2_D3 = By.XPATH, ".//p[contains(@class,'BurgerIngredient_ingredient__text__yp3dH') and text()='Флюоресцентная булка R2-D3']"
    R2_D3_IMG = By.XPATH, ".//*[@alt = 'Флюоресцентная булка R2-D3']"
    R2_D3_POP_UP = By.XPATH, ".//p[contains(@class,'text text') and text()='Флюоресцентная булка R2-D3']"
    EXIT_POP_UP = By.XPATH, ".//*[contains(@class, 'Modal_modal_opened')]/div/button"
    COUNT = By.XPATH, ".//*[contains(@alt, 'Флюоресцентная булка R2-D3')]/parent::a/div/p[@class='counter_counter__num__3nue1']"
    SPAN_DROP = By.XPATH, ".//span[contains(@class,'constructor-element__text') and text()='Перетяните булочку сюда (верх)']"
    ORDER_BUTTON = By.XPATH, ".//*[contains(@class,'button_button__33qZ0') and text()='Оформить заказ']"
    ORDER_READY = By.XPATH, ".//*[contains(@class,'undefined text') and text()='Ваш заказ начали готовить']"
    NUMBER_ORDER = By.XPATH, ".//*[text()='идентификатор заказа']/parent::div/h2"
    EXIT_ORDER_POP_UP = By.XPATH, ".//*[contains(@class, 'Modal_modal__close')]"
    ORDER_LET_CREATE = By.XPATH, ".//*[text()='Ваш заказ начали готовить']"

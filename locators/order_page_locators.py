from selenium.webdriver.common.by import By


class OrderPageLocators:

    NAME_FIELD_LOCATOR = (By.XPATH, ".//input[@placeholder = '* Имя']")
    SURNAME_FIELD_LOCATOR = (By.XPATH, ".//input[@placeholder = '* Фамилия']")
    ADDRESS_FIELD_LOCATOR = (By.XPATH, ".//input[@placeholder = '* Адрес: куда привезти заказ']")
    STATION_FIELD_LOCATOR = (By.XPATH, ".//input[@placeholder = '* Станция метро']")
    STATION_LIST_LOCATOR = (By.XPATH, ".//div[@class = 'select-search__select']/ul/li[1]")
    PHONE_FIELD_LOCATOR = (By.XPATH, ".//input[@placeholder = '* Телефон: на него позвонит курьер']")
    BUTTON_NEXT_LOCATOR = (By.XPATH, ".//button[text()='Далее']")
    DATE_FIELD_LOCATOR = (By.XPATH, ".//input[@placeholder = '* Когда привезти самокат']")
    DAY_FIELD_LOCATOR = (By.XPATH, ".//div[text()='* Срок аренды']")
    MENU_DATE_LOCATOR = (By.CLASS_NAME, "Dropdown-menu")
    COMMENT_FIELD_LOCATOR = (By.XPATH, ".//input[@placeholder = 'Комментарий для курьера']")
    BUTTON_ORDER_LOCATOR = (By.XPATH, ".//button[@class = 'Button_Button__ra12g Button_Middle__1CSJM']")
    BUTTON_YES_LOCATOR = (By.XPATH, ".//button[text() = 'Да']")
    STATUS_ORDER_LOCATOR = (By.XPATH, ".//div[@class = 'Order_ModalHeader__3FDaJ']")

from selenium.webdriver.common.by import By


class HomePageLocators:
    QUESTION_LOCATOR = 'accordion__heading-'
    LOGO_LOCATOR = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    BUTTON_ORDER_LOCATOR = (By.XPATH, ".//button[(@class = 'Button_Button__ra12g' and text()='Заказать')]")
    YA_LOGO_LOCATOR = (By.XPATH, ".//img[@alt = 'Yandex']")
    DZEN_LOGO_LOCATOR = (By.XPATH, ".//a[@data-testid = 'logo']")
    SCOOTER_LOGO_LOCATOR = (By.XPATH, ".//img[@alt = 'Scooter']")

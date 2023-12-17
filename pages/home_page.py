import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from locators.home_page_locators import HomePageLocators


class HomePageScooterHelper(BasePage):

    @allure.step("Просматриваем вопросы о важном")
    def importing_question_click(self, num):
        self.find_element((By.ID, HomePageLocators.QUESTION_LOCATOR + str(num))).click()

    @allure.step("Выбираем вопрос")
    def get_element_question(self, num):
        return self.find_element((By.ID, HomePageLocators.QUESTION_LOCATOR + num))

    @allure.step("Смотрим ответ")
    def get_answer(self, num):
        return self.find_element((By.XPATH, HomePageLocators.QUESTION_LOCATOR + num +'/following::p')).text

    @allure.step("Нажимаем на кнопку заказать")
    def order_click(self):
        self.find_element(By.XPATH, HomePageLocators.BUTTON_ORDER_LOCATOR).click()

    @allure.step("Нажимаем на логотип яндекс")
    def yandex_logo_click(self):
        self.find_element(HomePageLocators.YA_LOGO_LOCATOR, 3).click()

    def wait_for_dzen_load(self):
        self.find_element(HomePageLocators.DZEN_LOGO_LOCATOR, 3)

    @allure.step("Нажимаем на логотип самоката")
    def scooter_logo_click(self):
        self.find_element(HomePageLocators.SCOOTER_LOGO_LOCATOR, 3).click()

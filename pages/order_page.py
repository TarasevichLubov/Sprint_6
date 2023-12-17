import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from locators.order_page_locators import OrderPageLocators


class OrderPageHelper(BasePage):

    @allure.step("Заполняем имя")
    def set_name_field(self, name):
        self.find_element(OrderPageLocators.NAME_FIELD_LOCATOR).send_keys(name)

    @allure.step("Заполняем фамилию")
    def set_surname_field(self, surname):
        self.find_element(OrderPageLocators.SURNAME_FIELD_LOCATOR).send_keys(surname)

    @allure.step("Заполняем адрес")
    def set_address_field(self, address):
        self.find_element(OrderPageLocators.ADDRESS_FIELD_LOCATOR).send_keys(address)

    @allure.step("Заполняем станцию")
    def set_station_field(self, station):
        station_order = self.find_element(OrderPageLocators.STATION_FIELD_LOCATOR)
        station_order.click()
        station_order.send_keys(station)
        self.find_element(OrderPageLocators.STATION_LIST_LOCATOR).click()

    @allure.step("Заполняем телефон")
    def set_phone_field(self, phone):
        self.find_element(OrderPageLocators.PHONE_FIELD_LOCATOR).send_keys(phone)

    @allure.step("Далее")
    def next_click(self):
        self.find_element(OrderPageLocators.BUTTON_NEXT_LOCATOR).click()

    def set_user_date(self, name, surname, address, station, phone):
        self.set_name_field(name)
        self.set_surname_field(surname)
        self.set_address_field(address)
        self.set_station_field(station)
        self.set_phone_field(phone)

    @allure.step("Заполняем дату привоза")
    def set_date_field(self, date_arend):
        date_field = self.find_element(OrderPageLocators.DATE_FIELD_LOCATOR, 3)
        date_field.send_keys(date_arend)
        date_field.send_keys(Keys.ESCAPE)

    @allure.step("Заполняем количество дней")
    def set_day_field(self, day_arend):
        self.find_element(OrderPageLocators.DAY_FIELD_LOCATOR, 3).click()
        self.find_element(OrderPageLocators.MENU_DATE_LOCATOR, 3)
        self.find_element((By.XPATH, ".//div[text()='" + day_arend + "']"), 3).click()

    @allure.step("Заполняем цвет")
    def set_color_scooter(self, color):
        self.find_element((By.XPATH, ".//label[text() = '" + color + "']"), 3).click()

    @allure.step("Заполняем комментарий")
    def set_comment_field(self, comment):
        self.find_element(OrderPageLocators.COMMENT_FIELD_LOCATOR, 3).send_keys(comment)

    @allure.step("Нажимаем на кнопку Заказать")
    def button_order_click(self):
        self.find_element(OrderPageLocators.BUTTON_ORDER_LOCATOR, 3).click()

    @allure.step("Нажимаем кнопку подтверждения заказа")
    def button_yes_click(self):
        self.find_element(OrderPageLocators.BUTTON_YES_LOCATOR, 3).click()

    @allure.step("Получаем статус заказа")
    def get_status_order(self):
        return self.find_element(OrderPageLocators.STATUS_ORDER_LOCATOR, 3).text

    def set_address_data(self, date_arend, day_arend, color, comment):
        self.set_date_field(date_arend)
        self.set_day_field(day_arend)
        self.set_color_scooter(color)
        self.set_comment_field(comment)

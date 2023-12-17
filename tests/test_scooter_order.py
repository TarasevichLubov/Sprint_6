from pages.order_page import OrderPageHelper
from data import ConstantData
import pytest
import allure


class TestScooterOrder:

    @allure.story("Страница заказа Самоката")
    @allure.feature("Тестирование оформления заказа Самоката")
    @pytest.mark.parametrize('name_order, surname, address, station, phone, date_order, days_order, color, comment',
                             ConstantData.user_test_data)
    def test_scooter_order(self, driver, name_order, surname, address, station, phone,
                           date_order, days_order, color, comment):
        order = OrderPageHelper(driver)
        order.go_to_page(ConstantData.ORDER_URL)
        order.set_user_date(name_order, surname, address, station, phone)
        order.next_click()
        order.set_address_data(date_order, days_order, color, comment)
        order.button_order_click()
        order.button_yes_click()
        order_status_message = order.get_status_order()
        assert 'Заказ оформлен' in order_status_message

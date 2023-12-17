from pages.home_page import HomePageScooterHelper
from data import ConstantData
import allure


class TestLogo:
    @allure.story("Главная страница")
    @allure.feature("Тестирование логотипов Яндекс и Самоката")
    def test_logo_yandex(self, driver):
        home_page = HomePageScooterHelper(driver)
        home_page.go_to_page(ConstantData.BASE_URL)
        home_page.yandex_logo_click()
        home_page.change_window(1)
        home_page.wait_for_dzen_load()
        current_url = home_page.current_url()
        assert 'https://dzen.ru' in current_url

    def test_scooter_logo(self, driver):
        home_page = HomePageScooterHelper(driver)
        home_page.go_to_page(ConstantData.BASE_URL)
        home_page.scooter_logo_click()
        current_url = home_page.current_url()
        assert current_url == 'https://qa-scooter.praktikum-services.ru/'

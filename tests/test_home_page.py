import allure
import pytest
from data import ConstantData
from pages.home_page import HomePageScooterHelper


class TestImportingQuestion:
    @allure.story("Главная страница")
    @allure.feature("Станица заказа")
    @pytest.mark.parametrize('num, question, answer', ConstantData.questions)
    def test_importing_question(self, driver, num, question, answer):
        home_page = HomePageScooterHelper(driver)
        home_page.go_to_page(ConstantData.BASE_URL)
        question_element = home_page.get_element_question(num)
        home_page.go_to_element(question_element)
        home_page.importing_question_click(num)
        assert question_element.text == question

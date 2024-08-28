import allure

from data import TestingData


class TestBun:
    @allure.title('Проверка работы метода get_name для получения названия булки')
    def test_get_name_success(self, bun_test):
        assert bun_test.get_name() == TestingData.bun_name

    @allure.title('Проверка работы метода get_price для получения стоимости булки')
    def test_get_price_success(self, bun_test):
        assert bun_test.get_price() == TestingData.bun_price

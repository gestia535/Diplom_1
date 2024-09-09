import allure
import pytest
from data import database_buns, database_ingredients
from praktikum.database import Database


class TestDatabase:

    @allure.title('Проверка работы метода available_buns, который возвращает список доступных булок')
    @allure.description('Проверяем работу метода с данными из базы')
    @pytest.mark.parametrize('index, name, price', database_buns)
    def test_available_buns_success(self, index, name, price):
        database = Database()
        result = database.available_buns()
        assert result[index].get_name() == name and result[index].get_price() == price
        assert len(result) == 3

    @allure.title('Проверка работы метода available_ingredients, который возвращает список доступных ингредиентов')
    @allure.description('Проверяем работу метода с данными из базы')
    @pytest.mark.parametrize('index, type_of_ingredient, name, price', database_ingredients)
    def test_available_ingredients_success(self, index, type_of_ingredient, name, price):
        database = Database()
        result = database.available_ingredients()
        assert (result[index].get_type() == type_of_ingredient
                and result[index].get_name() == name
                and result[index].get_price() == price)
        assert len(result) == 6

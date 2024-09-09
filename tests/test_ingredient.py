import allure
import pytest
from data import TestingData
from praktikum.ingredient import Ingredient


class TestIngredient:

    @allure.title('Проверка работы метода get_price, который возвращает стоимость ингредиента')
    @allure.description('Проверяем работу метода с ингредиентами разных типов: соус и начинка')
    @pytest.mark.parametrize(
        'ingredient_type, name, price, expected_price',
        [
            [TestingData.sauce_type, TestingData.sauce_name, TestingData.sauce_price, TestingData.sauce_price],
            [TestingData.filling_type, TestingData.filling_name, TestingData.filling_price, TestingData.filling_price]
        ]
    )
    def test_get_price_success(self, ingredient_type, name, price, expected_price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == expected_price

    @allure.title('Проверка работы метода get_name, который возвращает наименование ингредиента')
    @allure.description('Проверяем работу метода с ингредиентами разных типов: соус и начинка')
    @pytest.mark.parametrize(
        'ingredient_type, name, price, expected_name',
        [
            [TestingData.sauce_type, TestingData.sauce_name, TestingData.sauce_price, TestingData.sauce_name],
            [TestingData.filling_type, TestingData.filling_name, TestingData.filling_price, TestingData.filling_name]
        ]
    )
    def test_get_name_success(self, ingredient_type, name, price, expected_name):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == expected_name

    @allure.title('Проверка работы метода get_type, который возвращает тип ингредиента')
    @allure.description('Проверяем работу метода с ингредиентами разных типов: соус и начинка')
    @pytest.mark.parametrize(
        'ingredient_type, name, price, expected_type',
        [
            [TestingData.sauce_type, TestingData.sauce_name, TestingData.sauce_price, TestingData.sauce_type],
            [TestingData.filling_type, TestingData.filling_name, TestingData.filling_price, TestingData.filling_type]
        ]
    )
    def test_get_type_success(self, ingredient_type, name, price, expected_type):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == expected_type

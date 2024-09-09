import allure
import pytest
from data import TestingData
from praktikum.burger import Burger


class TestBurger:
    @allure.title('Проверка работы метода set_buns, который устанавливает определенную булку для бургера')
    def test_set_buns_success(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun, f'Actual bun is {burger.bun}'

    @allure.title('Проверка работы метода add_ingredient, который добавляет ингредиенты в список')
    @allure.description('Проверяем работу метода с ингредиентами разных типов: соус и начинка')
    @pytest.mark.parametrize('ingredient, expected_result', [
        [TestingData.sauce_name, TestingData.sauce_name],
        [TestingData.filling_name, TestingData.filling_name]
    ])
    def test_add_ingredient_success(self, ingredient, expected_result):
        burger = Burger()
        burger.add_ingredient(ingredient)
        assert burger.ingredients == [expected_result] and len(burger.ingredients) == 1, \
            f'Expected ingredients list to contain {expected_result} with length 1, but got {burger.ingredients}'

    @allure.title('Проверка работы метода remove_ingredient, который удаляет ингредиенты из списка')
    @allure.description('Проверяем работу метода с ингредиентами разных типов: соус и начинка')
    @pytest.mark.parametrize('ingredient, removed_ingredient', [
        [TestingData.sauce_name, TestingData.sauce_name],
        [TestingData.filling_name, TestingData.filling_name]
    ])
    def test_remove_ingredient_success(self, mock_ingredient_1, ingredient, removed_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient_1 not in burger.ingredients, \
            f'Expected {mock_ingredient_1} to be removed, but it is still in {burger.ingredients}'
        assert ingredient in burger.ingredients, \
            f'Expected {ingredient} to remain, but it was not found in {burger.ingredients}'

    @allure.title('Проверка работы метода move_ingredient, который меняет ингредиенты местами в списке')
    def test_move_ingredient_success(self, mock_ingredient_1, mock_ingredient_2):
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_ingredient_2, \
            f'Expected {mock_ingredient_2} to be at index 0, but got {burger.ingredients[0]}'
        assert burger.ingredients[1] == mock_ingredient_1, \
            f'Expected {mock_ingredient_1} to be at index 1, but got {burger.ingredients[1]}'

    @allure.title('Проверка работы метода get_price, который возвращает цену бургера с учетом ингредиента и булок')
    def test_get_price(self, mock_ingredient_1, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        assert burger.get_price() == TestingData.burger_price

    @allure.title('Проверка работы метода get_receipt, который возвращает чек, содержащий название булки, ингредиент '
                  'и итоговую сумму')
    def test_get_receipt(self, mock_bun, mock_ingredient_1):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        receipt = ("(==== Флюоресцентная булка R2-D3 ====)\n"
                   "= filling Мясо бессмертных моллюсков Protostomia =\n"
                   "(==== Флюоресцентная булка R2-D3 ====)\n"
                   "\n"
                   "Price: 3313")
        assert burger.get_receipt() == receipt, f'Actual receipt is {burger.get_receipt()}'

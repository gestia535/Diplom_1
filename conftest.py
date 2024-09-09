from unittest.mock import Mock
import pytest
from data import TestingData
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = TestingData.bun_name
    mock_bun.get_price.return_value = TestingData.bun_price
    return mock_bun


@pytest.fixture
def mock_ingredient_1():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = TestingData.filling_name
    mock_ingredient.get_type.return_value = TestingData.filling_type
    mock_ingredient.get_price.return_value = TestingData.filling_price
    return mock_ingredient


@pytest.fixture
def mock_ingredient_2():
    mock_ingredient_2 = Mock()
    mock_ingredient_2.get_name.return_value = TestingData.sauce_name
    mock_ingredient_2.get_type.return_value = TestingData.sauce_type
    mock_ingredient_2.get_price.return_value = TestingData.sauce_price
    return mock_ingredient_2


@pytest.fixture
def ingredient():
    return Ingredient('sauce', 'Space Sauce', 80)


@pytest.fixture
def bun_test():
    bun = Bun('Флюоресцентная булка R2-D3', 988)
    return bun

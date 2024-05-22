from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():

    name = "Lasanha"
    price = 70.00
    dish1 = Dish(name, price)
    dish2 = Dish(name, price)

    ingredient1 = Ingredient("massa de lasanha")
    ingredient2 = Ingredient("queijo mussarela")
    ingredient3 = Ingredient("camarão")

    amount1 = 10
    amount2 = 15
    amount3 = 40

    assert dish1.name == name
    assert dish1.price == price
    assert len(dish1.recipe) == 0

    dish1.add_ingredient_dependency(ingredient1, amount1)
    dish1.add_ingredient_dependency(ingredient2, amount2)
    dish1.add_ingredient_dependency(ingredient3, amount3)
    assert len(dish1.recipe) == 3
    ingredients = {
        Ingredient('queijo mussarela'): 15,
        Ingredient('massa de lasanha'): 10,
        Ingredient('camarão'): 40
        }
    assert dish1.get_ingredients() == set(ingredients)
    restrictions = {
                    Restriction.GLUTEN,
                    Restriction.SEAFOOD,
                    Restriction.LACTOSE,
                    Restriction.ANIMAL_MEAT,
                    Restriction.ANIMAL_DERIVED
                    }
    assert dish1.get_restrictions() == restrictions

    assert repr(dish1) == "Dish('Lasanha', R$70.00)"
    assert hash(dish1) == hash("Dish('Lasanha', R$70.00)")
    assert dish1 == dish2
    value_error = "Dish price must be greater then zero."
    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("pão com ovo", "dez reais")
    with pytest.raises(ValueError, match=value_error):
        Dish("coxinha velha", 0.00)

from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    reference = "queijo parmesão"
    restrictions = {Restriction.LACTOSE, Restriction.ANIMAL_DERIVED}
    ingredient = Ingredient(reference)
    ingredient2 = Ingredient(reference)
    assert ingredient.name == reference
    assert ingredient.restrictions == restrictions
    assert repr(ingredient) == "Ingredient('queijo parmesão')"
    assert hash(ingredient) == hash(reference)
    assert ingredient == ingredient2

import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()

        try:
            with open(source_path, encoding="utf-8") as file:
                data = csv.DictReader(file, delimiter=",", quotechar='"')

                dict_list = {}
                for row in data:
                    name = row["dish"]
                    price = float(row["price"])
                    ingredient = row["ingredient"]
                    amount = int(row["recipe_amount"])
                    dish = Dish(name, price)
                    instance = Ingredient(ingredient)
                    if dish.name not in dict_list:
                        dish.add_ingredient_dependency(instance, amount)
                        dict_list[dish.name] = dish
                    else:
                        new = dict_list[dish.name]
                        new.add_ingredient_dependency(instance, amount)
            self.dishes.update(dict_list.values())
        except FileNotFoundError:
            print(f"Arquivo {source_path} não encontrado")


path = "tests/mocks/menu_base_data.csv"
dish_list = MenuData(path)
print(dish_list.dishes)

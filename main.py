'''
Рецепт (Соловьев)
    Суп с яичными хлопьями:
        - бульон
        - яйцо
        - мука
        - молоко
        - пармезан
        - манная крупа
'''

from ingredient import Ingredient
from recipe import Recipe


if __name__ == '__main__':
    receipt_from_api = {
        "title": "Суп с яичными хлопьями",
        "ingredients_list": [
            Ingredient('Бульон', 250, 120),
            Ingredient('Яйцо', 140, 80),
            Ingredient('Мука', 300, 150),
            Ingredient('Молоко', 100, 80),
            Ingredient('Пармезан', 300, 350),
            Ingredient('Манная крупа', 150, 80),
        ],
    }

    recipe = Recipe(receipt_from_api['title'], receipt_from_api['ingredients_list'])
    print(recipe)

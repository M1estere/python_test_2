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
            Ingredient('Бульон', 250, 100, 120),
            Ingredient('Яйцо', 140, 70, 80),
            Ingredient('Мука', 300, 150, 150),
            Ingredient('Молоко', 100, 50, 80),
            Ingredient('Пармезан', 300, 100, 350),
            Ingredient('Манная крупа', 150, 70, 80),
        ],
    }

    recipe = Recipe(receipt_from_api['title'], receipt_from_api['ingredients_list'])
    print(f'Стоимость одной порции: {recipe.calc_cost()}')
    print(f'Стоимость двух порций: {recipe.calc_cost(2)}')
    print(f'Вес двух порций: {recipe.calc_weight(2)}')
    print(f'Вес одной порции (сырой): {recipe.calc_weight(raw=True)}')

    print(recipe)

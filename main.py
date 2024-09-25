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


from recipe import Recipe


if __name__ == '__main__':
    receipt_from_api = {
        "title": "Суп с яичными хлопьями",
        "ingredients_list": [
            ('Бульон', 250, 100, 120),
            ('Яйцо', 140, 70, 80),
            ('Мука', 300, 150, 150),
            ('Молоко', 100, 50, 80),
            ('Пармезан', 300, 100, 350),
            ('Манная крупа', 150, 70, 80),
        ],
    }

    recipe = Recipe(receipt_from_api['title'], receipt_from_api['ingredients_list'])
    print(recipe)

    assert recipe.calc_cost() == 860, 'Wrong cost for one portion'
    assert recipe.calc_cost(2) == 1720, 'Wrong cost for two portions'
    assert recipe.calc_weight(2) == 2480, 'Wrong weight for two portions'
    assert recipe.calc_weight(raw=True) == 1240, 'Wrong weight for one raw portion'

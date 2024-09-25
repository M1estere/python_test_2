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

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients


    def calc_cost(self, portions=1):
        return sum([element.price for element in self.ingredients]) * portions


    def calc_weight(self, portions=1, raw=True):
        return sum([element.weight for element in self.ingredients]) * portions


    def __str__(self) -> str:
        return f'Рецепт {self.name} содержит:\n' + '\n'.join([f'- {ingredient.name} - {ingredient.weight}г, {ingredient.price}₽' for ingredient in self.ingredients])

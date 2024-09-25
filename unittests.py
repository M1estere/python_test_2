from recipe import Recipe
import unittest


class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")


    def setUp(self):
        print("setUp")
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
        self.recipe_object = recipe

    
    def tearDown(self):
        print("tearDown")
        del self.recipe_object


    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")


    def test_first(self):
        self.assertEqual(self.recipe_object.calc_cost(), 860)


    def test_second(self):
        self.assertEqual(self.recipe_object.calc_cost(2), 1720)


    def test_third(self):
        self.assertEqual(self.recipe_object.calc_weight(2), 2480)


    def test_fourth(self):
        self.assertEqual(self.recipe_object.calc_weight(raw=True), 1240)


if __name__ == '__main__':
    unittest.main()

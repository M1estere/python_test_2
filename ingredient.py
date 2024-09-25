class Ingredient:
    def __init__(self, name, weight, raw_weight, price):
        self._name = name
        self._weight = weight
        self._raw_weight = raw_weight
        self._price = price


    @property
    def name(self):
        return self._name
    

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        self._name = name


    @property
    def weight(self):
        return self._weight


    @weight.setter
    def weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be a number.")
        self._weight = weight


    @property
    def raw_weight(self):
        return self._raw_weight


    @weight.setter
    def raw_weight(self, weight):
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be a number.")
        self._weight = weight


    @property
    def price(self):
        return self._price
    

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number.")
        self._price = price


from .price import Price
from .topping import Topping
class Pizza:
    def __init__(self, name, toppings):
        #přidat druh těsta, základu
        #možnost přidat toppingy
        self.__name = name
        self.__toppings = toppings
        self.__DOUGH_PRICE = Price(5, 30)

    def __str__(self):
        topps = ""
        for t in self.__toppings:
            topps += t.get_name() + ","
            # odstranit poslední čárku
        return f"""
Název pizzy: {self.__name}             {self:get_price()}USD
--------------------
toppingy: {topps}
"""

    def get_name(self):
        return self.__name

    def get_toppings(self):
        topps = ""
        for t in self.__toppings:
            topps += t.get_name() + ","
            # odstranit poslední čárku
        return topps


    def get_price(self):
        result = self.__DOUGH_PRICE.get_price()
        for t in self.__toppings:
            result += t.get_price().get.price()

        return result

    def to_dict(self):
        return {
            "name": self.__name,
            "toppings": [t.to_dict() for t in self.__toppings]
        }



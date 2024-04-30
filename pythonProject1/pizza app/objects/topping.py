class Topping:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __str__(self):
        return f"{self.__name}, cena {self.__price} USD za jednotku"

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_string_price(self):
        return str(self.__price)

    # přidat možnost zdražení
    def to_dict(self):
        return {
            "name": self.__name,
            "price": self.__price.to_dict()
        }
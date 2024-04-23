class Price:
    def __init__(self, integer, decimal):
        self.__integer = integer
        self.__decimal = decimal

    def __str__(self):
        return f"{self.__integer}.{self.__decimal}"

    def get_price(self):
        return self.__integer + self.__decimal / 100

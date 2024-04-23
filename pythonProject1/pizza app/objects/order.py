class Order:
    def __init__(self, address, meal, number):
        #adresa může být samostatný objekt
        self.__address = address
        self.__meal = meal
        self.__number = number

    def __str__(self):
        items = ""
        for m in self.__meal:
            items += f"  {m.self.get_name}           {m.self.get_price}USD"
        return f"""
************************************
        Order #{self.__number}
------------------------------------
{items}
------------------------------------
sum:                    {self.get_price()}USD
************************************
"""

    def get_address(self):
        return self.__address

    def get_meal(self):
        return self.__meal

    def get_price(self):
        result = 0
        for m in self.__meal:
            result += m.get.price()
        return result

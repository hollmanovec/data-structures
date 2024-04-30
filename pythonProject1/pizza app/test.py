from objects import *

p = Price(1, 50)
t = Topping("Cheese", p)

#print(p)
#print(t)

# vytvoření seznamu příloh a pizz


pizza = Pizza("TEST PIZZA", [t])
pizza2 = Pizza("TEST PIZZA", [t])
# zapsat testovací pizzu do JSON file

pizzas = [pizza, pizza2]
import json
with open("test.json", "w") as file:
    for p in pizzas:
        json.dump(p.to_dict(), file)


from views import (print_pizza_menu, create_order_message)
from objects import Order, Queue



def create_new_order(orders_queue):
    print_pizza_menu()
    pizza_choice = input("Zadej volbu: ")
    user_address = input("Zadej adresu: ")
    user_order = Order(user_address, meal=[])
    orders_queue.add_new(user_order)
    create_order_message(user_order)
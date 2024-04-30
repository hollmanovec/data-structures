import json
from typing import Any


def print_main_menu():
    print("""
--------------MAIN MENU--------------
[1] - Nová objednávka
[2] - Zjistit stav objednávky
[3] - Vybavit poslední objednávku
[0] - Ukončit aplikaci   
    """)

def print_pizza_menu():
    file_handler = open("resources/pizza_list.json", "r")
    pizza_list = json.loads(file_handler)
    print(f"""
Seznam Pizz:
{pizza_list}
    """)


def input_address():
    address = input("Zadejte adresu pro doručení")
    return address


def create_order_message(order):
    print("Objednávka vatvořena")
    print("Info o objednávce:")

def wrong_choice_message():
    print("Zadal jsi špatnou volbu")

def exit_message():
    print("Děkujeme za objednávku, nashledanou")

print_pizza_menu()
def print_main_menu():
    print("""
--------------MAIN MENU--------------
[1] - Nová objednávka
[2] - Zjistit stav objednávky
[3] - Vybavit poslední objednávku
[0] - Ukončit aplikaci   
    """)

def print_pizza_menu():
    print("""
Seznam Pizz:

    """)


def input_address():
    address = input("Zadejte adresu pro doručení")
    return address


def create_order_message(order):
    print("Objednávka vatvořena")
    print("Info o objednávce:")
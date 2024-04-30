from views import *
from objects import Order, Queue
from pizzaAppFunctionality import create_new_order


def run__app():
    # TODO zálohování a načtení z paměti
    orders_queue = Queue(31)
    while True:
        print_main_menu()
        # TODO ošetřit kontrolu vstupů
        user_choice = int(input("Zadej volbu: "))

        if user_choice == 1:
            create_new_order(orders_queue)


        elif user_choice == 2:
            pass

        elif user_choice == 3:
            pass

        elif user_choice == 4:
            orders_queue.read_latest()

        elif user_choice == 0:
            #TODO uložení orders do paměti
            exit_message()
            exit()

        else:
            wrong_choice_message()




run__app()

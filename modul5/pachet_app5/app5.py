from adaugare import *
from stergere import *

inventar = {}

if __name__ == '__main__':
    while True:

        selection = input("""
        Meniu:
        1. Vizualizare stoc
        2. Adaugare produs
        3. Stergere produs
        4. Iesire
        """)
        if selection == "1":
            print(inventar)

        if selection == "2":
            adaugare_func(inventar)

        if selection == "3":
            stergere_func(inventar)
        if selection == "4":
            break
        print(inventar)






### Programm zum Durchsuchen der Inventarliste des Signallabors
### LustigerLeo & XX

from functions.search import *
from functions.detailsearch import *
from functions.listmenu import *
from functions.editmenu import *

def main():
    while True:
        print("\nMenü:")
        print("1. Einfache Suche")
        print("2. Detailsuche")
        print("3. Liste ausgeben")
        print("4. Editieren")
        print("5. Beenden")

        choice = input("Wählen Sie eine Option (1-5): ")

        if choice == "1":
            search()
        elif choice == "2":
            detailsearch()
        elif choice == "3":
            listmenu()
        elif choice == "4":
            editmenu()
        elif choice == '5':
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte wählen Sie eine Option von 1 bis 5.")

if __name__ == "__main__":
    main()
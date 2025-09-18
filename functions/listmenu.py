from functions.listfunctions.showList import *
from functions.listfunctions.givePDF import *
from functions.listfunctions.giveCSV import *

def listmenu():
    print("\nMenü:")
    print("1. Liste im Terminal ausgeben")
    print("2. Liste als PDF ausgeben")
    print("3. Liste als CSV ausgeben")
    print("4. Zurück")

    choice = input("Wählen Sie eine Option (1-4): ")
    if choice == "1":
        showList()
    elif choice == "2":
        givePDF()
    elif choice == "3":
        giveCSV()
    elif choice == "4":
        pass
    else:
        print("Ungültige Auswahl. Bitte wählen Sie eine Option von 1 bis 4.")

from functions.editFunctions.addEntry import *
from functions.editFunctions.changeEntry import *
from functions.editFunctions.deleteEntry import *

def editmenu():
        print("\nMenü:")
        print("1. Eintrag hinzufügen")
        print("2. Eintrag bearbeiten")
        print("3. Eintrag löschen")
        print("4. Zurück")

        choice = input("Wählen Sie eine Option (1-3): ")

        if choice == "1":
            addEntry()
        elif choice == "2":
            changeEntry()
        elif choice == "3":
            deleteEntry()
        elif choice == "4":
            pass
        else:
            print("Ungültige Auswahl. Bitte wählen Sie eine Option von 1 bis 4.")

    
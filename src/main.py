# Hauptmenü für Übung 2

from aufgabe1_matrix_mult.matrix_multiplication import run as run_aufgabe1


def main():
    print("\n===== ÜBUNG 2 – Lineare Algebra =====")
    print("1 – Matrixmultiplikation")
    print("2 – Gauß (L- und R-Matrix)")
    print("3 – LR-Zerlegung nach Crout")
    print("4 – Inverse (Gauß-Jordan)")
    print("5 – Graph: Distanz- & Routingmatrix")
    print("0 – Beenden")

    choice = input("Bitte Aufgabe wählen: ")

    if choice == "1":
        run_aufgabe1()

    elif choice == "2":
        print("Aufgabe 2 ist noch nicht implementiert.")

    elif choice == "3":
        print("Aufgabe 3 ist noch nicht implementiert.")

    elif choice == "4":
        print("Aufgabe 4 ist noch nicht implementiert.")

    elif choice == "5":
        print("Aufgabe 5 ist noch nicht implementiert.")

    elif choice == "0":
        print("Programm beendet.")

    else:
        print("Ungültige Eingabe.")

    # Zurück zum Menü
    main()


if __name__ == "__main__":
    main()

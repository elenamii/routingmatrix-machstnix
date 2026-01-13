# Hauptmenü für Übung 2

from aufgabe1_matrix_mult.matrix_multiplication import run as run_aufgabe1
from aufgabe2_gauss.gauss_lr import run as run_aufgabe2
from aufgabe3_crout.crout_lr import run as run_aufgabe3
from aufgabe4_inverse.gauss_jordan import run as run_aufgabe4
from aufgabe5_graphen.floyd_warshall import run as run_aufgabe5

def main():
    while True: # um rekursive funktionsaufrufe zu vermeiden 
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
            run_aufgabe2()
    
        elif choice == "3":
            run_aufgabe3()
    
        elif choice == "4":
            run_aufgabe4()
    
        elif choice == "5":
            run_aufgabe5()
    
        elif choice == "0":
            print("Programm beendet.")
    
        else:
            print("Ungültige Eingabe")




if __name__ == "__main__":
    main()

#Erstellen Sie ein Programm zur Multiplikation von Matrizen.
#A x B = C
# rows x cols
# A (mxn) x B(nxp) = C (mxp)

# reine rechenfunktion für Aufgabe 2-5 nutzbar
def multiply(A, B):
    rowsA =len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len (B[0])

    if colsA != rowsB:
        raise ValueError("Ungültige Dimensionen: Spalten(A) entsprechen nicht Zeilen(B)")
    
    C = []
    for i in range(rowsA):
        row = []
        for j in range(colsB):
            summe = 0
            for k in range(colsA):
                summe += A[i][k] * B[k][j]
            row.append(summe)
        C.append(row)

    #   für jede Zeile:
    #     neue Zeile
    #     für jede Spalte:
    #         Wert berechnen
    #         Wert in Zeile speichern
    #     Zeile in Ergebnis speichern  

    return C



#hilffunktion für ein und ausgabe
def read_matrix (rows, cols, name):
    M = []
    print (f'Matrix {name}:')
    for i in range(rows):
        row = []
        for j in range (cols):
            value = int(input(f"{name}[{i}][{j}]: "))
            row.append(value)
        M.append(row)
    return M

def print_matrix(M):
    for row in M:
        print(row)

#interaktiver modus für main.py und vorführung 

def run():
    print("Matrixmultiplikation A x B")
    print('Geben Sie die Dimensionen der Matrizen ein:')
    rowsA = int(input('Zeilen Matrix A:'))
    colsA = int(input('Spalten Matrix A:'))

    rowsB = int(input('Zeilen Matrix B:'))
    colsB = int(input('Spalten Matrix B:'))

    if (colsA != rowsB):
        print ('Ungültige Dimensionen. Fehler: Anzahl Spalten von Matrix A muss gleich Anzahl Zeilen von Matrix B sein.')
        return

    A = read_matrix(rowsA, colsA, "A")
    B = read_matrix(rowsB, colsB, "B")

    try:
        C = multiply(A, B)
    except ValueError as e:
        print(e)
        return
    
    print("\nErgebnis C = A × B:")
    print_matrix(C)
    

#für direkten start in der datei'
if __name__ =="__main__":
    run()


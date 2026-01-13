#Erstellen Sie ein Programm zur Multiplikation von Matrizen.
#A x B = C
# rows x cols


print('Geben Sie die Dimensionen der Matrizen ein:')
rowsA = int(input('Zeilen Matrix A:'))
colsA = int(input('Spalten Matrix A:'))

rowsB = int(input('Zeilen Matrix B:'))
colsB = int(input('Spalten Matrix B:'))

if (colsA != rowsB):
    print ('Ungültige Dimensionen.Fehler: Anzahl Spalten von Matrix A muss gleich Anzahl Zeilen von Matrix B sein.')
    exit()

A = []
print ('Matrix A:')
for i in range(rowsA):
    row = []
    for j in range (colsA):
        row.append(int(input(f"A[{i}][{j}]: ")))
    A.append(row)

B= []
print ('Matrix B:')
for i in range (rowsB):
    row= []
    for j in range (colsB):
        row.append(int(input(f"B[{i}][{j}]:")))
    B.append(row)


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

print("Ergebnis-Matrix:")
for row in C:
    print(row)

from utils.matrix_utils import is_square_matrix
from utils.matrix_inout import read_square_matrix, print_matrix

def crout(A):
    if not is_square_matrix(A):
        raise ValueError("Matrix nicht quadratisch")

    n = len(A)
    L = [[0]*n for _ in range(n)]
    R = [[0]*n for _ in range(n)]
    for i in range(n):
        R[i][i] = 1

    for j in range(n):
        for i in range(j, n):
            L[i][j] = A[i][j] - sum(L[i][k]*R[k][j] for k in range(j))
        for i in range(j+1, n):
            R[j][i] = (A[j][i] - sum(L[j][k]*R[k][i] for k in range(j))) / L[j][j]

    return L, R


def run():
    n = int(input("Dimension: "))
    A = read_square_matrix(n, "A")
    L, R = crout(A)
    print("L:")
    print_matrix(L)
    print("R:")
    print_matrix(R)


if __name__ == "__main__":
    run()

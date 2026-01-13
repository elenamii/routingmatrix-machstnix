from utils.matrix_utils import is_square_matrix, copy_matrix
from utils.matrix_inout import read_square_matrix, print_matrix

def gauss_lr(A):
    if not is_square_matrix(A):
        raise ValueError("Matrix nicht quadratisch")

    n = len(A)
    R = copy_matrix(A)
    L = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = R[i][k] / R[k][k]
            L[i][k] = factor
            for j in range(k, n):
                R[i][j] -= factor * R[k][j]

    return L, R


def run():
    n = int(input("Dimension: "))
    A = read_square_matrix(n, "A")
    L, R = gauss_lr(A)
    print("L:")
    print_matrix(L)
    print("R:")
    print_matrix(R)


if __name__ == "__main__":
    run()

from utils.matrix_utils import is_square_matrix, identity_matrix
from utils.matrix_inout import read_square_matrix, print_matrix

def inverse(A):
    if not is_square_matrix(A):
        raise ValueError("Matrix nicht quadratisch")

    n = len(A)
    I = identity_matrix(n)
    M = [A[i] + I[i] for i in range(n)]

    for i in range(n):
        pivot = M[i][i]
        if pivot == 0:
            return None
        for j in range(2*n):
            M[i][j] /= pivot
        for k in range(n):
            if k != i:
                factor = M[k][i]
                for j in range(2*n):
                    M[k][j] -= factor * M[i][j]

    return [row[n:] for row in M]


def run():
    n = int(input("Dimension: "))
    A = read_square_matrix(n, "A")
    inv = inverse(A)
    
    if inv is None:
        print("Die Matrix ist nicht invertierbar.")
    else:
        print("Inverse:")
        print_matrix(inv)

if __name__ == "__main__":
    run()

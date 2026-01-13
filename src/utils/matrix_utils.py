def is_square_matrix(A):
    n = len(A)
    return all(len(row) == n for row in A)


def identity_matrix(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def copy_matrix(A):
    return [row[:] for row in A]

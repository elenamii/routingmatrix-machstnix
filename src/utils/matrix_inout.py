def read_matrix(rows, cols, name):
    M = []
    print(f"Matrix {name}:")
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(float(input(f"{name}[{i}][{j}]: ")))
        M.append(row)
    return M


def read_square_matrix(n, name):
    return read_matrix(n, n, name)


def print_matrix(M):
    for row in M:
        out = []
        for x in row:
            if isinstance(x, (int, float)):
                if x == float("inf"):
                    out.append("∞")
                else:
                    out.append("{:.2f}".format(x))
            else:
                out.append(str(x))
        print(out)


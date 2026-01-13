def read_graph(n):
    print("Adjazenzmatrix (∞ für keine Kante):")
    G = []
    for i in range(n):
        row = []
        for j in range(n):
            v = input(f"G[{i}][{j}]: ")
            row.append("∞" if v == "∞" else float(v))
        G.append(row)
    return G

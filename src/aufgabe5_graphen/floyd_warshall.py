from utils.graphen_inout import read_graph
from utils.matrix_inout import print_matrix

def floyd_warshall(G):
    n = len(G)
    D = [[float("inf") if G[i][j] == "∞" else G[i][j] for j in range(n)] for i in range(n)]
    R = [["-" if (i == j or G[i][j] == "∞") else j for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][k] + D[k][j] < D[i][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    R[i][j] = R[i][k]
    return D, R


def run():
    n = int(input("Anzahl Knoten: "))
    G = read_graph(n)
    D, R = floyd_warshall(G)
    print("Distanzmatrix:")
    print_matrix(D)
    print("Routingmatrix:")
    print_matrix(R)


if __name__ == "__main__":
    run()

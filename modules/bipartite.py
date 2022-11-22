from graph_old import Network
from edmondskarp import edmonds_karp

def network_from_bipartite(X, Y, E):
    net = Network()
    net.vertices = X | Y | {0, -1}
    net.source = 0
    net.sink = -1
    net.edges = E | {(0, x) for x in X} | {(y, -1) for y in Y}
    net.capacity = {e: 1 for e in net.edges}
    return net

if __name__ == "__main__":
    n = network_from_bipartite({1,2,3},{4,5,6},{(1,4),(1,5),(2,4),(3,6)})
    print(n.capacity)
    print(edmonds_karp(n))
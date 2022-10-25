from graph import Network, inv_edge

def find_shortest_path(network: Network) -> list[int]:
    """
    Uses breadth first search to find the shortest path in a network
    """
    visited = []
    neighbors = [(network.source, [])]
    while neighbors:
        current, path = neighbors.pop(0)
        next_path = path + [current]
        if current == network.sink:
            return next_path
        for edge in network.edges:
            if edge[0] == current:
                next = edge[1]
                if next not in visited:
                    neighbors.append((next, next_path))

def residual_network(network: Network, flow: dict) -> Network:
    """
    Takes a network and a valid flow through the network, and computes the corresponding residual network
    """
    residual = Network()
    residual.vertices = network.vertices.copy()
    residual.source = network.source
    residual.sink = network.sink

    for edge in network.edges:
        f = flow[edge]
        c = network.get_capacity(edge)
        if f < c:
            residual.add_edges([edge])
            residual.capacity[edge] = c - f
        if f > 0:
            residual.add_edges([inv_edge(edge)])
            residual.capacity[inv_edge(edge)] = f

    return residual

def path_min_capacity(network: Network, path: list[int]) -> int:
    return min(network.get_capacity((path[i], path[i+1])) for i in range(len(path)-1))

def augment_path(flow: dict, path: list[int], amount: int) -> dict:
    """
    Augments the path given in the flow by amount
    """
    augmented_flow = flow.copy()
    for i in range(len(path)-1):
        edge = (path[i], path[i+1])
        if edge in flow:
            augmented_flow[edge] += amount
        else:
            augmented_flow[inv_edge(edge)] -= amount
    return augmented_flow

def edmonds_karp(network: Network) -> dict:
    """
    The Edmonds-Karp algorithm for computing the max flow in a network
    """
    flow = {e: 0 for e in network.edges}
    while True:
        residual = residual_network(network, flow)
        augmenting_path = find_shortest_path(residual)
        if augmenting_path == None:
            break
        augmenting_value = path_min_capacity(residual, augmenting_path)
        flow = augment_path(flow, augmenting_path, augmenting_value)
    return flow

if __name__ == "__main__":
    net = Network()
    net.add_verts([1,2,3,4])
    net.add_edges([(1,2), (1,3), (2, 3), (2,4), (3,4)])
    net.source = 1
    net.sink = 4
    net.capacity = {
        (1,2): 2,
        (1,3): 3,
        (2,3): 1,
        (2,4): 3,
        (3,4): 3
    }

    print(edmonds_karp(net))
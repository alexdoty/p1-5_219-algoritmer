from graph import Network, inv_edge

def find_shortest_path(network: Network) -> list[int]:
    """
    Uses breadth first search to find the shortest path in a network, from the source to the sink
    """
    # Visited represents vertices that were already visited, and therefore should not be visited again
    visited = []

    # Neighbors are nodes that have been seen but that are not yet visited. Each neighbor also contains the path to it.
    neighbors = [(network.source, [])]

    # Continue while there are still unvisited neighbors
    while neighbors:
        # Extract the neighbor vertex at the fornt of the queue
        current, path = neighbors.pop(0)
        next_path = path + [current]

        # If the end is reached, return the path taken to it
        if current == network.sink:
            return next_path

        # Go through each edge, if it goes out from the current vertex, and it has not been visited, add it to the list of neighbors
        for edge in network.edges:
            if edge[0] == current:
                next = edge[1]
                if next not in visited:
                    neighbors.append((next, next_path))

def find_path_depth_first(network: Network, current_path: list[int] = []) -> list[int]:
    """
    Finds a path from source to sink quickly, but which is not optimized. Using this in ford-fulkerson achieves the original complexity
    """
    # Start with just the source
    if current_path == []:
        current_path = [network.source]

    vertex = current_path[-1]

    # If the sink has been reached, return the path taken
    if vertex == network.sink:
        return current_path

    # For each edge going out from this node, call the function again if the edge is not already in the path
    for edge in network.edges:
        if edge[0] == vertex and edge[1] not in current_path:
            next_path = current_path + [edge[1]]
            sink_path = find_path_depth_first(network, next_path)

            # If a path is returned, terminate and return that path
            if sink_path:
                return sink_path

    # If none of the outgoing edges returned succesful paths, return None
    return None

def residual_network(network: Network, flow: dict) -> Network:
    """
    Takes a network and a valid flow through the network, and computes the corresponding residual network
    """
    # Create a new network with the same vertices
    residual = Network("graphs/empty_graph.csv")
    residual.vertices = network.vertices.copy()
    residual.source = network.source
    residual.sink = network.sink

    # Go throughr each edge
    for edge in network.edges:
        f = flow[edge]
        c = network.get_capacity(edge)

        # If the flow is not maximal, add an edge with the remaining capacity
        if f < c:
            residual.add_edges([edge])
            residual.capacity[edge] = c - f

        # If the flow is not zero, add an edge with that capacity going in the opposite direction
        if f > 0:
            residual.add_edges([inv_edge(edge)])
            residual.capacity[inv_edge(edge)] = f

    return residual

def path_min_capacity(network: Network, path: list[int]) -> int:
    """
    Get the minimum capactiy along a path, which is the maximum value it can be augmented by
    """
    return min(network.get_capacity((path[i], path[i+1])) for i in range(len(path)-1))

def augment_path(flow: dict, path: list[int], amount: int) -> dict:
    """
    Augments the path given in the flow by amount
    """
    # Create a new flow
    augmented_flow = flow.copy()
    for i in range(len(path)-1):
        # Get the edge between two consecutive vertices on the path
        edge = (path[i], path[i+1])

        if edge in flow:
            augmented_flow[edge] += amount
        else: # To augment the flow in the opposite direction of the edge, subtraction is used instead
            augmented_flow[inv_edge(edge)] -= amount
    return augmented_flow

def ford_fulkerson(network: Network) -> dict:
    """
    The Ford-fulkerson algorithm for computing the max flow in a network

    Takes flow graph as input, so a graph G = (V, E) and a flow capacity c. We also need a start and a finish, so a source node s and "sink" node t
    Returns flow with maximum capacity from s to t, which is a sequence
    """
    # Start by assuming all flow i zero
    flow = {e: 0 for e in network.edges}

    while True:
        # Find the residual network
        residual = residual_network(network, flow)

        # Find a path in the residual network
        augmenting_path = find_path_depth_first(residual)

        # If no augmenting path exists, stop
        if augmenting_path == None:
            break

        # Find value which the path can be augmented by
        augmenting_value = path_min_capacity(residual, augmenting_path)

        # Augment the flow along the path by the value
        flow = augment_path(flow, augmenting_path, augmenting_value)
    return flow

def edmonds_karp(network: Network) -> dict:
    """
    The Edmonds-Karp algorithm for computing the max flow in a network
    """
    # Start by assuming all flow i zero
    flow = {e: 0 for e in network.edges}

    while True:
        # Find the residual network
        residual = residual_network(network, flow)

        # Find the shortest path in the residual network
        augmenting_path = find_shortest_path(residual)

        # If no augmenting path exists, stop
        if augmenting_path == None:
            break

        # Find value which the path can be augmented by
        augmenting_value = path_min_capacity(residual, augmenting_path)

        # Augment the flow along the path by the value
        flow = augment_path(flow, augmenting_path, augmenting_value)
    return flow

if __name__ == "__main__":
    net = Network("graphs/wiki_graph.csv")

    print(net)

    flow = edmonds_karp(net)
    print(flow)
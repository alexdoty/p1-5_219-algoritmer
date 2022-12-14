from graph import Network
from edmondskarp import *

def list_paths(network: Network, current_path: list[int] = None) -> list[list[int]]:
    """
    Finds all paths from source to sink quickly, but which is not optimized.
    """
    # Start with just the source
    if current_path == None:
        current_path = [network.source]

    vertex = current_path[-1]

    # If the sink has been reached, return the path taken
    if vertex == network.sink:
        return [current_path]

    paths = []
    # For each edge going out from this node, call the function again if the edge is not already in the path
    for edge in network.edges:
        if edge[0] == vertex and edge[1] not in current_path:
            next_path = current_path + [edge[1]]
            sink_paths = list_paths(network, next_path)

            # If a list of paths is returned, add them to the list of paths
            if sink_paths:
                paths.extend(sink_paths)

    # Return the list of paths from this vertex to sink
    return paths

def get_utilisation_change(network: Network, path: list[int], amount: int) -> float:
    """
    Get the change in utilisation along a path, if the flow is augmented by amount
    """
    util = 0

    # Sum delta mu for all edges in path
    for i in range(len(path)-1):
        util += amount / network.get_capacity((path[i], path[i+1]))
    return util

def optimal_utilisation(network: Network) -> dict:
    flow = {e: 0 for e in net.edges}

    # Loop until no paths
    while True:
        res = residual_network(net, flow)
        paths = list_paths(res)
        if paths == []:
            break

        best_path = None
        best_util = float('inf')

        for path in paths:
            amount = path_min_capacity(res, path)
            util = get_utilisation_change(net, path, amount)

            if util < best_util:
                best_util = util
                best_path = path
        flow = augment_path(flow, best_path, path_min_capacity(res, best_path))
    return flow

if __name__ == "__main__":
    net = Network()
    # net.add_verts([1,2,3,4,5,6])
    # net.add_edges([(1,2), (1,3), (2, 4), (3,5), (4,6), (5,6), (3,4), (5,2)])
    # net.source = 1
    # net.sink = 6
    # net.capacity = {
    #     (1,2): 4,
    #     (1,3): 2,
    #     (2,4): 3,
    #     (3,5): 2,
    #     (4,6): 2,
    #     (5,6): 3,
    #     (3,4): 1,
    #     (5,2): 2,
    # }

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

    flow = ford_fulkerson(net)
    print(flow)

    flow = optimal_utilisation(net)
    print(flow)
    

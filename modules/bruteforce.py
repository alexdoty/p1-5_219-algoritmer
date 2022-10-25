from graph import Network

def powerset(base_set: set) -> list[set]:
    """
    Calculates the power set of a set recursively 
    """
    if base_set == set():
        return [set()]
    copied_set = base_set.copy()
    element = copied_set.pop()
    sub_powerset = powerset(copied_set)
    return sub_powerset + [subset | {element} for subset in sub_powerset]

def brute_force_max_flow(network: Network) -> int:
    """
    Calculates the max flow in a network through an ineffective brute force method
    """

    s = network.source
    t = network.sink

    source_partitions = [{s} | subset for subset in powerset(network.vertices - {s, t})]

    min_cut_capacity = 999999999999999999999999999999999999999

    for source_partition in source_partitions:
        sink_partition = network.vertices - source_partition
        cut_capacity = 0
        for v in source_partition:
            for u in sink_partition:
                cut_capacity += network.get_capacity((v,u))
        if cut_capacity < min_cut_capacity:
            min_cut_capacity = cut_capacity
    return min_cut_capacity

net = Network()

net.source = 1
net.sink = 4

net.add_verts([1, 2, 3, 4])
net.add_edges([(net.source, 2), (2, net.sink), (net.source , 3), (3, net.sink)])

net.capacity = {(net.source, 2): 3, (2, net.sink): 4, (net.source , 3): 4, (3, net.sink): 2}

print(brute_force_max_flow(net))
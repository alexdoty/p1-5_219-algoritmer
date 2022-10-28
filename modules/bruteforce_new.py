from graph import Network

def powerset(base_set: set) -> list[set]:
    """
    Calculates the power set of a set recursively 
    """
    # The powerset of the empty is just a list of the empty set
    if base_set == set():
        return [set()]

    copied_set = base_set.copy()

    # Pick an element from the set and remove it
    element = copied_set.pop()

    # Find the powerset of the remaining set
    sub_powerset = powerset(copied_set)

    # The total powerset is the union of the powerset without the element, and that powerset but with the element added to each set
    return sub_powerset + [subset | {element} for subset in sub_powerset]

def brute_force_max_flow(network: Network) -> int:
    """
    Calculates the max flow in a network through an ineffective brute force method
    """

    s = network.source
    t = network.sink

    # Get all sets of verticies containing the source vertex and not the sink. These represent cuts
    source_partitions = [{s} | subset for subset in powerset(network.vertices - {s, t})]

    # Assume that the minimum cut capacity is infinity
    min_cut_capacity = 999999999999999999999999999999999999999

    for source_partition in source_partitions:
        sink_partition = network.vertices - source_partition
        cut_capacity = 0

        #Calculate the cut capacity by summing all flow from the source partition to the sink partition
        for v in source_partition:
            for u in sink_partition:
                cut_capacity += network.get_capacity((v,u))

        # If the capacity is less than the current minimum, update the minimum
        if cut_capacity < min_cut_capacity:
            min_cut_capacity = cut_capacity
    return min_cut_capacity

if __name__ == "__main__":
    net = Network()

    net.source = 1
    net.sink = 4

    net.add_verts([1, 2, 3, 4])
    net.add_edges([(net.source, 2), (2, net.sink), (net.source , 3), (3, net.sink)])

    net.capacity = {(net.source, 2): 3, (2, net.sink): 4, (net.source , 3): 4, (3, net.sink): 2}

    print(brute_force_max_flow(net))
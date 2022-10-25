# Module for creating networks :)

class Network:
    def __init__(self) -> None:
        self.vertices = set()
        self.edges = set()
        self.capacity = {}
        self.source = None
        self.sink = None

    def get_capacity(self, e) -> int:
        '''Gets the capacity for all edges'''
        capacity = self.capacity
        inv = inv_edge(e)
        
        if e in capacity:
            return capacity[e]
        elif inv in capacity:
            return -capacity[inv]
        else:
            return 0

    def add_verts(self, elements):
        self.vertices.update(elements)

    def add_edges(self, elements):
        self.edges.update(elements)


def inv_edge(e):
    edge_list = list(e)
    return (edge_list[1], edge_list[0])


# test
net = Network()

v = net.vertices
e = net.edges

net.add_verts([2, 3, 4])
net.add_edges([(2, 3), (3, 2), (2, 4)])

inv_e = inv_edge((2, 3))

print(v)
print(e)
print(inv_e)




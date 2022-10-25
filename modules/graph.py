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


def inv_edge(e):
    edge_list = list(e)
    return (edge_list[1], edge_list[0])

def add_verts(v, elements):
    v.update(elements)

def add_edges(e, elements):
    e.update(elements)


# test
net = Network()

v = net.vertices
e = net.edges

add_verts(v, [2, 3, 4])
add_edges(e, [(2, 3), (3, 2), (2, 4)])

inv_e = inv_edge((2, 3))

print(v)
print(e)
print(inv_e)




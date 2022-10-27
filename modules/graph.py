# Module for creating networks :)
from __future__ import annotations
from csv_class import *

class Network:
    def __init__(self) -> None:
        self.vertices = set()
        self.edges = set()
        self.capacity = {}
        self.source = None
        self.sink = None
        self.csv_file = None

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

    def get_flow_value(self, flow) -> int:
        flow_value = 0

        for edge in flow:
            if edge[1] == self.sink:
                flow_value += self.get_capacity(edge)
        return flow_value

def inv_edge(e):
    edge_list = list(e)
    return (edge_list[1], edge_list[0])

# test

b = parse_csv('example_graph.csv')
c = csv_thing(b)

for i in c:
    print(c.get(3, i))



# net = Network()

# v = net.vertices
# e = net.edges

# net.add_verts([2, 3, 4])
# net.add_edges([(2, 3), (3, 2), (2, 4)])

# inv_e = inv_edge((2, 3))



# Module for creating networks :)
from __future__ import annotations
# from csv_class import *

def vertex_int(v):
    if v == 's':
        return 0
    elif v == 't':
        return -1
    elif v == '':
        return 
    return int(v)

class Network:
    def __init__(self) -> None:
        self.vertices = set()
        self.edges = set()
        self.capacity = {}
        self.source = None
        self.sink = None

    @classmethod
    def from_csv(cls, filename):
        net = Network()
        lines = []
        with open(filename) as f:
            for line in f:
                print(line)
                lines.append(list(map(vertex_int, line.split(','))))
        for line in lines[1:]:
            A = line[0]
            net.vertices.add(A)
            for i in range(1, len(line)):
                val = int(line[i])
                if val != 0:
                    B = lines[0][i]
                    net.edges.add((A,B))
                    net.capacity[(A,B)] = val
        net.source = 0
        net.sink = -1
        return net

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

if __name__ == '__main__':
    # test


    net = Network.from_csv("graphs/wiki_graph.csv")
    print(net.capacity)

    # v = net.vertices
    # e = net.edges

    # net.add_verts([2, 3, 4])
    # net.add_edges([(2, 3), (3, 2), (2, 4)])

    # inv_e = inv_edge((2, 3))



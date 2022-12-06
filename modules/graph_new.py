from csv_parser import *

def make_capacity(csv):
    data = csv.retrieve_internals()
    rows = data[0]
    cols = data[1]

    capacity = dict()

    for key, value in rows.items():
        for count, node in enumerate(cols[value]):
            if node != 0:
                capacity.update({ (value, rows[count]) : node })

    return capacity


class Network:
    '''Class that defines a network from a given csv file'''
    def __init__(self, filename):
        self.filename = filename
        self.csv_file = csv_parser(filename)
        self.capacity = make_capacity(self.csv_file)

        self.vertices = set()
        self.edges = list()
        for key, value in self.capacity.items():
            self.edges.append(key)
            self.vertices.add(value)

        self.source = max(self.vertices) + 1
        self.sink = 0

    def __str__(self):
        return f'capacity: {self.capacity}\nvertices: {self.vertices}\nedges: {self.edges}\nsource: {self.source}\nsink: {self.sink}'

    def add_edges(self, list_edges):
        self.edges.update(list_edges)

    def add_vertices(self, list_vertices):
        self.vertices.update(list_vertices)

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

def inv_edge(e):
    edge_list = list(e)
    return (edge_list[1], edge_list[0])

net = Network("graphs/wiki_graph.csv")


print(net)
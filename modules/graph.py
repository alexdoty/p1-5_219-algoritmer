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
        return "capacity: {}\nvertices: {}\nedges: {}\nsource: {}\nsink: {}".format(
            self.capacity, self.vertices, self.edges, self.source, self.sink
        )

def inv_edge(e):
    edge_list = list(e)
    return (edge_list[1], edge_list[0])

graph = Network('graphs/demon_graph.csv')
print(graph)
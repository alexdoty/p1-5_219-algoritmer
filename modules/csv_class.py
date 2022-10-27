import csv

class csv_thing:
    def __init__(self, data):
        tmp = parse_data(data)
        self.rows = tmp[0]
        self.cols = tmp[1]
    
    def __str__(self):
        return "[{}, {}]".format(self.rows, self.cols)
    
    def get(self, x, y):
        return self.cols[self.rows[y]][x]

def parse_csv(csv_file):
    real_graph_list = []

    with open(csv_file) as f:
        graph_list = csv.reader(f, delimiter=' ')
        for i in graph_list:
            real_graph_list.extend(i)

    return real_graph_list

def parse_data(data):
    rows = {}
    cols = {}
    for count, item in enumerate(data[0][1:].split(",")):
        rows.update({ count : item[0] })
    for column in data[1:]:
        raw = column.split(",")
        cols.update({ column[0][0] : list(map(int, raw[1:])) })
    return [rows, cols]
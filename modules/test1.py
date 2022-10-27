def parse_csv(data):
    rows = {}
    cols = {}
    for count, item in enumerate(data[0][1:].split(",")):
        rows.update({ count : item[0] })
    for column in data[1:]:
        raw = column.split(",")
        cols.update({ column[0][0] : list(map(int, raw[1:])) })
    return [rows, cols]


class csv:
    def __init__(self, data):
        tmp = parse_csv(data)
        self.rows = tmp[0]
        self.cols = tmp[1]
    
    def __str__(self):
        return "{}, {}".format(self.rows, self.cols)
    
    def get(self, x, y):
        return self.cols[self.rows[y]][x]

data = [",s,a", "s,1,2", "a,3,0"]
foo = csv(data)
print(foo)
print(foo.get(0, 1))
print(foo.get(1, 1))
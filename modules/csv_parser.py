def read_data(filename):
    with open(filename) as file:
        return [line.rstrip() for line in file]


def parse_csv(data):
    rows = dict()
    cols = dict()
    for count, item in enumerate(data[0][1:].split(",")):
        rows.update({ count : item[0] })
    for column in data[1:]:
        raw = column.split(",")
        cols.update({ column[0][0] : list(map(int, raw[1:])) })
    return [rows, cols]


class csv_parser:
    def __init__(self, filename):
        in_data = read_data(filename)
        tmp = parse_csv(in_data)
        self.rows = tmp[0]
        self.cols = tmp[1]

    def __str__(self):
        return "{}, {}".format(self.rows, self.cols)

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self) -> list:
        current_index = self.current_index
        if current_index < len(self.rows):
            key_val = self.rows[current_index]
            ret = self.cols[key_val]
            self.current_index += 1
            return ret
        raise StopIteration

    def get(self, x, y) -> str:
        key_val = self.rows[y]
        return self.cols[key_val][x]

    def retrieve_internals(self) -> list[dict, dict]:
        return [self.rows, self.cols]
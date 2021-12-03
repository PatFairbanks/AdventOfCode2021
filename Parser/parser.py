import pathlib


class Parser:
    def __init__(self):
        self._input_file = None

    @property
    def input_file(self):
        return self._input_file

    @input_file.setter
    def input_file(self, input_file: pathlib.Path):
        if input_file.is_file():
            self._input_file = input_file

    def parseFileToTupleList(self):
        tl = list()
        with open(self.input_file, "r") as f:
            dir_data = f.read().splitlines()
        for vector in dir_data:
            v = vector.split()
            tl.append((v[0], v[1]))
        return tl

    def parseFileToIntList(self):
        with open(self.input_file, "r") as f:
            try:
                return [int(x) for x in f.read().splitlines()]
            except AttributeError as e:
                print(e)
                return None


if __name__ == "__main__":
    pass

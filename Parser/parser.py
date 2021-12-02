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

    def parseFileToIntList(self):
        with open(self.input_file, "r") as f:
            return [int(x) for x in f.read().splitlines()]


if __name__ == "__main__":
    pass

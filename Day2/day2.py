import pathlib
from Parser.parser import Parser
from typing import List, Tuple


def Day_Two(start: List, movements: List[Tuple]) -> List:
    """Given a parsed list of tuples containing direction and movement,
    this method determines the foward/depth distance from the starting point.

    If the direction is up, the depth decreases. If down, the depth increases.

    Args:
        start: initial position
        movements: sequence of movements formatted as [(direction, depth)]

    Returns
    """
    for vector in movements:
        print(start)
        if vector[0] == "forward":
            start[0] += int(vector[1])
        elif vector[0] == "up":
            start[1] -= int(vector[1])
        elif vector[0] == "down":
            start[1] += int(vector[1])
        else:
            print("Unknown direction")
    return start[0] * start[1]


def Day_Two_Faulty_Aim(start: List, movements: List[Tuple]) -> List:
    """Given a parsed list of tuples containing direction and movement,
    this method determines the foward/depth distance from the starting point.

    If the direction is up, the depth decreases. If down, the depth increases.

    Args:
        start: initial position
        movements: sequence of movements formatted as [(direction, depth)]

    Returns
    """
    aim = 0
    for vector in movements:
        if vector[0] == "forward":
            start[0] += int(vector[1])
            start[1] += int(vector[1]) * aim
        elif vector[0] == "up":
            aim -= int(vector[1])
        elif vector[0] == "down":
            aim += int(vector[1])
        else:
            print("Unknown direction")
    return start[0] * start[1]


if __name__ == "__main__":
    inputFile = pathlib.Path("input.txt")
    parser = Parser()
    parser.input_file = inputFile
    print(parser.input_file)
    data = parser.parseFileToTupleList()
    start = [0, 0]
    print(Day_Two_Faulty_Aim(start, data))

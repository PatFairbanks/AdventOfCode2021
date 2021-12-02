from os import cpu_count
import pathlib

from typing import List
from Parser.parser import Parser


def Day_One(depth_measurements: List[int]) -> int:
    """Within the depth measurements, calculate how many times
    the depth increases.

    Args:
        depth_measurements: integer list of depths

    Returns:
        increasing depth count.
    """
    count = 0
    if not depth_measurements:
        return count

    for depth_index in range(1, len(depth_measurements)):
        if depth_measurements[depth_index - 1] < depth_measurements[depth_index]:
            count += 1
    return count


def Day_One_Sliding_Window(depth_measurements: List[int]):
    """Within the depth measurements, calculate how many times
    the depth increases, where a depth is calculated as the
    sum of three consecutive elements in the data set.

    Args:
        depth_measurements: integer list of depths

    Returns:
        increasing depth count.
    """
    deq = list()
    count = 0
    if len(depth_measurements) < 3:
        return count

    for depth in depth_measurements:
        if len(deq) < 3:
            deq.append(depth)
            continue
        prev_sum = sum(deq)
        deq.append(depth)
        deq.pop(0)

        if prev_sum < sum(deq):
            count += 1
    return count


if __name__ == "__main__":
    inputFile = pathlib.Path("input.txt")
    parser = Parser()
    parser.input_file = inputFile
    data = parser.parseFileToIntList()
    print(Day_One(data))
    print(Day_One_Sliding_Window(data))

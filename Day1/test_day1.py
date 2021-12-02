import unittest
from Day1.day1 import Day_One_Sliding_Window

import day1


class TestDay1(unittest.TestCase):
    def setUp(self):
        self.depths = [1, 2, 1, 2, 1, 2, 1, 2]

    def test_day_one_pass(self):
        self.assertEqual(4, day1.Day_One(self.depths))

    def test_day_one_empty(self):
        self.assertEqual(0, day1.Day_One([]))

    def test_day_one_sliding_window_pass(self):
        self.assertEqual(3, day1.Day_One_Sliding_Window(self.depths))

    def test_day_one_sliding_window_short_list(self):
        self.assertEqual(0, day1.Day_One_Sliding_Window([]))

    def test_day_one_sliding_window_min_length(self):
        self.assertEqual(0, day1.Day_One_Sliding_Window([0, 1, 2]))


if __name__ == "__main__":
    unittest.main()

import unittest
from Day2.day2 import Day_Two_Faulty_Aim
from day2 import Day_Two


class TestDay2(unittest.TestCase):
    def setUp(self):
        pass

    def test_Day_Two_Pass(self):
        start = [0, 0]
        movements = [("forward", 3), ("down", 12), ("up", 3), ("forward", 10)]
        self.assertEqual(13 * 9, Day_Two(start, movements))

    def test_Day_Two_Faulty_Movements_Pass(self):
        start = [0, 0]
        movements = [("forward", 3), ("down", 12), ("up", 3), ("forward", 10)]
        self.assertEqual(13 * 90, Day_Two_Faulty_Aim(start, movements))


if __name__ == "__main__":
    unittest.main()

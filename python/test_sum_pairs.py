from sum_pairs import sum_pairs


import unittest


class TestSumPairs(unittest.TestCase):
    def test_sum_pairs(self):
        self.assertEqual(sum_pairs([1, 2, 3, 4, 5], 9) == [[4, 5]])
        self.assertEqual(sum_pairs([1, 2, 3, 4, 5], 7) == [[2, 5], [3, 4]])
        self.assertEqual(sum_pairs([3, 1, 5, 8, 2], 27) == [])

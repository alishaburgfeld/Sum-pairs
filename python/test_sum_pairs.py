from sum_pairs import sum_pairs


import unittest


def make_sets(nested_arr):
    return {frozenset(el) for el in nested_arr}


class TestSumPairs(unittest.TestCase):
    def test_sum_pairs(self):
        self.assertEqual(make_sets(sum_pairs([1, 2, 3, 4, 5], 9)) == make_sets([[4, 5]]))
        self.assertEqual(make_sets(sum_pairs([1, 2, 3, 4, 5], 7)) == make_sets([[2, 5], [3, 4]]))
        self.assertEqual(make_sets(sum_pairs([3, 1, 5, 8, 2], 27)) == make_sets([]))

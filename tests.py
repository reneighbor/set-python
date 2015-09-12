import unittest

from _set import Set

class SetTest(unittest.TestCase):

    def test_construct_empty(self):
        test_set = Set()

        assert test_set.elements == []

    def test_construct_initial_elements(self):
        test_set = Set([1, 2, 3])

        # TODO when size() is implemented, assert
        # size is 3
        assert test_set.elements == [1, 2, 3]

    def test_construct_initial_elements_duplicates(self):
        test_set = Set([1, 2, 2])

        # TODO when size() is implemented, assert
        # size is 2
        assert test_set.elements == [1, 2]
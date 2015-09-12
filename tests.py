import unittest

from _set import Set

class SetTest(unittest.TestCase):

    def test_construct(self):
        test_set = Set()
        print test_set

        assert 1 == 2
import unittest
import time

from _set_hash import Set
# from _set import Set

class SetTest(unittest.TestCase):

    def test_construct_empty(self):
        test_set = Set()

        assert test_set.len() == 0
        assert test_set != None

    def test_construct_initial_elements(self):
        test_set = Set([1, 2, 3])

        assert test_set.len() == 3
        assert test_set.contains(1)
        assert test_set.contains(2)
        assert test_set.contains(3)

    def test_construct_initial_elements_duplicates(self):
        test_set = Set([1, 2, 2])

        assert test_set.len() == 2
        assert test_set.contains(1)
        assert test_set.contains(2)

    def test_add(self):
        test_set = Set([1, 2, 3])
        test_set.add(4)

        assert test_set.len() == 4
        assert test_set.contains(1)
        assert test_set.contains(2)
        assert test_set.contains(3)
        assert test_set.contains(4)

    def test_add_duplicate(self):
        test_set = Set([1, 2, 3])        
        test_set.add(3)

        assert test_set.len() == 3
        assert test_set.contains(1)
        assert test_set.contains(2)
        assert test_set.contains(3)

    def test_remove(self):
        test_set = Set([1, 2, 3])
        test_set.remove(3)

        assert test_set.len() == 2
        assert test_set.contains(1)
        assert test_set.contains(2)
        assert test_set.contains(3) == False

    def test_remove_not_present(self):
        test_set = Set([1, 2, 3])
        test_set.remove(4)
    
        assert test_set.len() == 3
        assert test_set.contains(1)
        assert test_set.contains(2)
        assert test_set.contains(3)

    def test_len(self):
        test_set = Set([1, 2, 3])

        assert test_set.len() == 3

    def test_len_zero(self):
        test_set = Set()

        assert test_set.len() == 0

    def test_contains(self):
        test_set = Set([1, 2, 3])

        assert test_set.contains(1)

    def test_contains_false(self):
        test_set = Set([1, 2, 3])

        assert test_set.contains(4) == False

    def test_equals(self):
        test_set = Set([1, 2, 3])

        assert test_set.equals(Set([1, 2, 3]))

    def test_equals_wrong_class(self):
        test_set = Set([1, 2, 3])

        assert test_set.equals([1, 2, 3]) == False

    def test_equals_false(self):
        test_set = Set([1, 2, 3])

        assert test_set.equals(Set([1, 2])) == False

#     def test_subset_of(self):
#         test_set = Set([1, 2, 3])

#         assert test_set.subset_of(Set([1, 2, 3, 4]))

#     def test_subset_of_equivalent(self):
#         test_set = Set([1, 2, 3])

#         assert test_set.subset_of(Set([1, 2, 3]))

#     def test_subset_of_false(self):
#         test_set = Set([1, 2, 3])

#         assert test_set.subset_of(Set([1, 2])) == False

#     def test_union(self):
#         test_set = Set([1, 2, 3])
#         union_set = test_set.union(Set([4, 5]))

#         # TODO ASK is it a problem that this fails?
#         # assert union_set == Set([1, 2, 3, 4, 5])
#         assert union_set.equals(Set([1, 2, 3, 4, 5]))

#     def test_union_duplicates(self):
#         test_set = Set([1, 2, 3])
#         union_set = test_set.union(Set([1, 2]))

#         # TODO ASK is it a problem that this fails?
#         # assert union_set == Set([1, 2, 3])
#         assert union_set.equals(Set([1, 2, 3]))

#     def test_intersect(self):
#         test_set = Set([1, 2, 3])
#         intersect_set = test_set.intersect(Set([1, 2, 4]))

#         assert intersect_set.equals(Set([1, 2]))

#     def test_intersect_empty_set(self):
#         test_set = Set([1, 2, 3])
#         intersect_set = test_set.intersect(Set())

#         assert intersect_set.equals(Set())

#     def test_intersect_no_matches(self):
#         test_set = Set([1, 2, 3])
#         intersect_set = test_set.intersect(Set([4, 5]))

#         assert intersect_set.equals(Set())

#     def test_difference(self):
#         test_set = Set([1, 2, 3])
#         difference_set = test_set.difference(Set([1, 2, 4]))

#         assert difference_set.equals(Set([3, 4]))

#     def test_difference_all_matches(self):
#         test_set = Set([1, 2, 3])
#         difference_set = test_set.difference(Set([1, 2, 3]))

#         assert difference_set.equals(Set())



    # Used to compare against list 
    # implementation of a set - 
    # Should be pretty fast, ie
    # 0.028s for 50000 - maybe
    # do 2 inputs and ensure 01n
    # def test_contains_large(self):
    #     test_set = Set(range(0, 50000))

    #     start = time.time()
    #     assert test_set.contains(40000)
    #     stop = time.time()
        
    #     total = stop - start
    #     print "Total: " + str(total)
        
    #     assert 1 == 2
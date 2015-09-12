# set-python
Writing a set from scatch in Python

## Description
A set is a data structure; it is a collection of items. It can be thought of as like a list; however, unlike a list, items in a set must be *unique*. If you have a set that consists of 'Jane', 'Janice', and 'John', you cannot append the name 'John' to the set, but you can append the name 'Lucy.'

Additionally, items in a set are not typically kept in any *sort order*, so if you put items into a set in some particular order, you cannot rely on being able to acces or retrieve them according to that order.

The task is to implement a set in Python using Test-Driven Development (TDD), but without using the `set` data type.

## Process

### 1. Write the spec of methods you need to support and test cases for the first two features of the spec.

1. init(self, elements = []) - Create a new set, optionally passing in a list which will be the starting elements of the set.
  * When you create a new set without passing in elements, my new set is an empty list.
  * When you create a new set that does have starting elements, the new set will be the same size as the starting list and contain all elements of the starting list.
2. add(self, item) - adds an item to the set, if it is not yet in the set.
  * When you add an item to the set that is not yet in the set, the size of the set increments by 1 and the set contains all items that were in it perviously, as well as the new item.
  * When you add an item already in the set, the set stays the same length and it contains all the same items that were in the set before.
3. remove(self, item) - removes item from the set, if it is present.
4. len(self) - returns a count of the number of items in the set.
5. contains(self, item) - returns true if the item is in the set, false if it is not.
6. equal(self, setB) - returns true if the set is equivalent to another set, setB. Returns false if it is not.
7. subsetOf(setB) - returns true if all items in the set are also in set_b. Returns false if it does not.
8. union(setA, setB). Creates a new set that contains all elements in both setA and setB.
intersect.

### 2 Set up your project folder, with one file for tests and one file for your class. 

Write a test that simply asserts 1==1, to ensure your testing framework is set up as expected. At this point the project looks like this:

set-python
 -tests.py
 -set.py

And the tests file looks like this:
	https://github.com/reneighbor/set-python/commit/f680e809d3cb93ce6e311064448b4a300dd7ac02

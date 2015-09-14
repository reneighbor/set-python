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
7. subsetOf(self, setB) - returns true if all items in the set are also in set_b. Returns false if it does not.
8. union(self, setB). Creates a new set that contains all elements in both self and setB.
9. intersect(self, setB). Creates a new set that contains all elements that are in both self and setB
10. difference(self, setB). Creates a new set that contains all elements that are in self but not setB

### 2. Set up your project and tests with basic "hello world" functionality to make sure everything is wired up.

Set up your project folder, with one file for tests and one folder for your class. Write a test that simply asserts 1==1, to ensure your testing framework is set up as expected:

At this point the project files look like this:

set-python</br>
	-tests.py </br>
 	-set.py 

And the tests file looks like this:
	https://github.com/reneighbor/set-python/commit/f680e809d3cb93ce6e311064448b4a300dd7ac02

Make sure you can import your class from your tests. Make sure you can print out an instance of your class. Have your assertion test 1==2, otherwise the unit test framework will print out your print statements.

At this point your project looks like this:

https://github.com/reneighbor/set-python/commit/ce8ee258cb579e6cb8cad967bd67ad26a0c0bd6a

And your test output looks like this:


```
rchu:set-python renee$ nosetests
F
======================================================================
FAIL: test_construct (tests.SetTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/renee/Projects/personal-projects/set-python/tests.py", line 11, in test_construct
    assert 1 == 2
AssertionError: 
-------------------- >> begin captured stdout << ---------------------
<_set.Set instance at 0x1055b45a8>

--------------------- >> end captured stdout << ----------------------

----------------------------------------------------------------------
Ran 1 test in 0.004s

FAILED (failures=1)
```
### 3. Write out unit tests for the test cases of your constructor, then write the constructor. 

Pretty self-explanatory. I will say I tested and implemented the empty case first (`test_construct_empty`), then tested and implemented the case with initializing elements.

A side note is that I had to do some thinking about whether my set *is* an empty list (`self = []`), or whether my set *has* elements which are an empty list (`self.elements = []`). I decided on the latter (and re-wrote my test plan accordingly); just like a list *has* items, a set *has* items (or elements). But it *is* a set, this new thing that is being created. Talk about abstract thinking :)

At this point the project looks like this:
https://github.com/reneighbor/set-python/commit/6de741ce1723d1af93d850b76730c5d6c4d036f5

### 4. Write out tests for and function definition for your first method, add(). 
Added the case where it's appended and where a duplicate is added.

At this point the code looks like this:
https://github.com/reneighbor/set-python/commit/5efbe96b6d0c222689d227c87df99aea38ed2188

### 5. ...And all the rest. Here all the rest of the tests and implementations. I realized (and edited the spec after the fact) that I had forgotten specs for intersection() and difference(), so quickly added those as well. 

When working on making a test pass, I also went back to the implementation for equals(), adding a sorted() when comparing the elements of the two compared sets. This ensures that equals() returns true regardless of the elements' sort order.

Here is that one big commit:
https://github.com/reneighbor/set-python/commit/118f08fd62b23cb9e7dffdc25ec0e37da1cb6965

import pytest
from sorts.insertion_sort import sort as insertion_sort
from sorts.selection_sort import sort as selection_sort
from searches.linear_search import search as linear_search
from sorts.merge_sort import sort as merge_sort
from sorts.heap_sort import sort as heap_sort

def _test_sorting_algorithm(sort_func):
    # Test case 1: Array in ascending order
    A = [1, 2, 3, 4, 5]
    assert sort_func(A) == sorted(A)

    # Test case 2: Array in descending order
    A = [5, 4, 3, 2, 1]
    assert sort_func(A) == sorted(A)

    # Test case 3: Array with duplicate elements
    A = [3, 1, 2, 2, 4]
    assert sort_func(A) == sorted(A)

    # Test case 4: Empty array
    A = []
    assert sort_func(A) == sorted(A)

    # Test case 5: Array with a single element
    A = [42]
    assert sort_func(A) == sorted(A)
   
    # Test case 6: Array with negative numbers
    A = [-5, 0, 3, -2, 1]
    assert sort_func(A) == sorted(A)

def _test_search_algorithm(search_func):
    # Test case 1: Trivial case 
    A = [1, 2, 3, 4, 5]
    assert search_func(A, 1) == A.index(1)

    # Test case 2: Array with duplicate elements 
    A = [1, 1, 2, 3, 4, 5]
    assert search_func(A, 1) == A.index(1)

    # Test case 3: Empty array 
    A = []
    assert search_func(A, 1) is None

    # Test case 4: value isn't in array 
    A = [123, 34, 1535, 3]
    assert search_func(A, 1) is None

def test_linear_search():
    _test_search_algorithm(linear_search)

def test_selection_sort():
    _test_sorting_algorithm(selection_sort)

def test_insertion_sort():
    _test_sorting_algorithm(insertion_sort)

def test_merge_sort():
    _test_sorting_algorithm(merge_sort)

def test_heap_sort():
    _test_sorting_algorithm(heap_sort)

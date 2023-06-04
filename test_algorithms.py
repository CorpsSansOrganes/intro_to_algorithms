import pytest
from sorts.insertion_sort import sort as insertion_sort
from sorts.selection_sort import sort as selection_sort
from searches.linear_search import search as linear_search
from sorts.merge_sort import sort as merge_sort
from sorts.heap_sort import sort as heap_sort
from sorts.quick_sort import sort as quick_sort
from searches.binary_search import search as binary_search
from selects.find_min import find_min
from selects.find_max import find_max

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

def _test_search_algorithm_over_sorted_array(search_func):
    # Test case 1: Trivial case
    A = [1, 2, 3, 4, 5]
    assert search_func(A, 1) == A.index(1)

    # Test case 2: Array with duplicate elements 
    A = [1, 1, 2, 3, 4, 5]
    assert A[search_func(A, 1)] == 1

    # Test case 3: Empty array 
    A = []
    assert search_func(A, 1) is None

    # Test case 4: value isn't in array 
    A = [3, 34, 123, 1535]
    assert search_func(A, 1) is None

    # Test case 5: Last element in the array 
    A = [1, 3, 5, 7, 9]
    assert search_func(A, 9) == A.index(9)

    # Test case 6: Element in the middle cannot be found
    A = [1, 2, 6, 10]
    assert search_func(A, 5) is None

    # Test case 7: First element in even array 
    A = [1, 3, 5, 7, 9, 11]
    assert search_func(A, 1) == A.index(1)

    # Test case 8: First element in odd array 
    A = [1, 3, 5, 7, 9]
    assert search_func(A, 1) == A.index(1)

def test_find_min():
    arr = [4, 2, 9, 1, 7]
    assert find_min(arr) == 1

    arr = [5, 8, 3, 6, 2]
    assert find_min(arr) == 2

    arr = [10, 4, 6, 3, 1]
    assert find_min(arr) == 1

    arr = [3]
    assert find_min(arr) == 3

    arr = [7, 6]
    assert find_min(arr) == 6

def test_find_max():
    arr = [4, 2, 9, 1, 7]
    assert find_max(arr) == 9

    arr = [5, 8, 3, 6, 2]
    assert find_max(arr) == 8

    arr = [10, 4, 6, 3, 1]
    assert find_max(arr) == 10

    arr = [3]
    assert find_max(arr) == 3

    arr = [7, 6]
    assert find_max(arr) == 7

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

def test_quick_sort():
    _test_sorting_algorithm(quick_sort)

def test_binary_search():
    _test_search_algorithm_over_sorted_array(binary_search)

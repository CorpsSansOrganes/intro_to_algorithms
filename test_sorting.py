import pytest
from sorts.insertion_sort import sort as insertion_sort
from sorts.selection_sort import sort as selection_sort

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

def test_selection_sort():
    _test_sorting_algorithm(selection_sort)

def test_insertion_sort():
    _test_sorting_algorithm(insertion_sort)

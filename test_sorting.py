import argparse
import importlib
import pytest

def test_sorting_algorithm(sort_func):
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

if __name__ == '__main__':
    # Parse the command-line argument
    parser = argparse.ArgumentParser()
    parser.add_argument('sort', help='Name of the sorting algorithm module (without .py extension)')
    args = parser.parse_args()

    # Import the sorting algorithm module
    sort_module = importlib.import_module(args.sort)

    # Check if the specified sorting algorithm function exists
    if False == hasattr(sort_module, 'sort'):
        print(f"Sorting algorithm 'sort' not found in module '{args.sort}'.")
        exit(1)

    # If it does, run the test
    sort_func = getattr(sort_module, 'sort')
    test_sorting_algorithm(sort_func)

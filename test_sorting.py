import pytest
import os
import importlib

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

def pytest_generate_tests(metafunc):
    if "sort_func" in metafunc.fixturenames:
        # Get the path of the "sorts" directory
        sorts_dir = os.path.dirname(os.path.abspath(__file__)) + '/sorts'

        # Iterate over each file in the "sorts" directory
        for file_name in os.listdir(sorts_dir):
            if file_name.endswith('.py') and file_name != '__init__.py':
                # Remove the file extension to get the module name
                module_name = file_name[:-3]

                # Dynamically import the sorting algorithm module
                sort_module = importlib.import_module(f'sorts.{module_name}')

                # Check if the specified sorting algorithm function exists
                if hasattr(sort_module, 'sort'):
                    # Retrieve the sorting algorithm function
                    sort_func = getattr(sort_module, 'sort')

                    # Add the sorting algorithm function as a parameter to the test function
                    metafunc.parametrize("sort_func", [sort_func], ids=[module_name])
                else:
                    pytest.fail(f"Sorting algorithm 'sort' not found in module '{module_name}'")

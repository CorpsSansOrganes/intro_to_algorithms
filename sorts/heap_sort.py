from typing import List

def sort(arr: List[int]) -> List[int]:
    temp = list(arr)
    heap_sort(temp)
    return temp 

def heap_sort(arr: List[int]):
    _build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)

def _build_max_heap(arr: List[int]):
    for i in range(len(arr) // 2 - 1, -1, -1):
        _heapify(arr, len(arr), i)

def _heapify(arr: List[int], heap_size: int, i: int):
    largest = i
    l = 2*i + 1
    r = 2*i + 2

    # Finding the biggest among i and its children.
    if l < heap_size and arr[largest] < arr[l]:
        largest = l 
    if r < heap_size and arr[largest] < arr[r]:
        largest = r

    # Base case: no swap was performed
    if largest == i:
        return

    # Swap, and continue recursively
    arr[i], arr[largest] = arr[largest], arr[i]
    _heapify(arr, heap_size, largest)

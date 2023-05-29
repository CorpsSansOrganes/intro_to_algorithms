from typing import List

def sort(arr: List[int]) -> List[int]:
    temp = list(arr)
    heap_sort(temp)
    return temp 

def heap_sort(arr: List[int]):
    build_max_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(arr, i, 0)
    return arr

def build_max_heap(arr: List[int]):
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, len(arr), i)

def heapify(arr: List[int], heap_size: int, i: int):
    l = 2*i + 1
    r = 2*i + 2

    if l <= len(arr) and


from typing import List
import random

def sort(arr: List[int]) -> List[int]:
    temp = list(arr)
    quick_sort(temp, 0, len(temp))
    return temp

def quick_sort(arr: List[int], l: int, r: int):
    if (r - l <= 1):
        return 
    pivot = _randomize_partition(arr, l, r)
    quick_sort(arr, l, pivot)
    quick_sort(arr, pivot, r)


def _randomize_partition(arr: List[int], l: int, r: int) -> int:
    i = random.randint(l, r - 1)
    arr[i], arr[r - 1] = arr[r - 1], arr[i]
    return _partition(arr, l, r)

def _partition(arr: List[int], l: int, r: int) -> int:
    pivot = arr[r - 1]
    i = l - 1

    # Putting all elements <= then the pivot to the left.
    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    # Putting the pivot in place
    i += 1
    arr[i], arr[r - 1] = arr[r - 1], arr[i]
    return i

    

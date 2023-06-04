from typing import List, Optional
from sorts.quick_sort import _randomized_partition

def select(arr:List[int], i: int) -> Optional[int]:
    if not arr or i > len(arr):
        return None
    return _quick_select(arr, 0, len(arr), i)

def _quick_select(arr: List[int], l: int, r: int, i: int) -> int:
    if r - l == 1:
        return arr[l] # base case: subarray has one element.
    pivot = _randomized_partition(arr, l, r)
    pivot_order_statistic = pivot - l 

    if i < pivot_order_statistic: 
        return _quick_select(arr, l, pivot, i)
    elif i > pivot_order_statistic:
        return _quick_select(arr, pivot + 1, r, i - pivot_order_statistic)
    else:
        return arr[pivot] # pivot is the answer

'''
TEMPORARY
import random
def _randomized_partition(arr: List[int], l: int, r: int) -> int:
    i = random.randint(l, r - 1)
    arr[i], arr[r - 1] = arr[r - 1], arr[i]
    return _partition(arr, l, r)

def _partition(arr: List[int], l: int, r: int) -> int:
    pivot = arr[r - 1]
    i = l - 1

    for j in range(l, r - 1):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    i += 1
    arr[i], arr[r - 1] = arr[r - 1], arr[i]
    return i
'''

from typing import List, Optional
from sorts.quick_sort import _randomized_partition

def select(arr: List[int], i: int) -> Optional[int]:
    if not arr or i > len(arr):
        return None
    return _quick_select_iter(arr, 0, len(arr), i)
    #return _quick_select_recursive(arr, 0, len(arr), i)

def _quick_select_recursive(arr: List[int], l: int, r: int, i: int) -> int:
    pivot = _randomized_partition(arr, l, r)
    pivot_order_statistic = pivot - l + 1 

    if pivot_order_statistic == i:
        return arr[pivot]
    elif pivot_order_statistic > i: 
        return _quick_select_recursive(arr, l, pivot, i)
    else: # pivot_order_statistic < i:
        return _quick_select_recursive(arr, pivot + 1, r, i - pivot_order_statistic)

def _quick_select_iter(arr: List[int], l: int, r: int, i: int) -> int:
    while True:
        pivot = _randomized_partition(arr, l, r)
        pivot_order_statistic = pivot - l + 1 

        if pivot_order_statistic > i:
            r = pivot 
        elif pivot_order_statistic < i:
            l = pivot + 1
            i -= pivot_order_statistic
        else:
            return arr[pivot]

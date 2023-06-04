from typing import List, Optional
from sorts.quick_sort import _randomized_partition

def select(arr:List[int], i: int) -> Optional[int]:
    return _quick_select(arr, 0, len(arr), i)

def _quick_select(arr: List[int], l: int, r: int, i: int) -> int:
    if r - l == 1:
        return l # base case: subarray has one element.
    pivot = _randomized_partition(arr, l, r)
    pivot_order_statistic = pivot - l 

    if i < pivot_order_statistic: 
        return _quick_select(arr, l, pivot, i)
    elif i > pivot_order_statistic:
        return _quick_select(arr, pivot + 1, r, i - pivot_order_statistic)
    else:
        return pivot 

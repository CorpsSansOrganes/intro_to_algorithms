from typing import List, Optional

def search(arr: List[int], value: int) -> Optional[int]:
    return _binary_search_iter(arr, 0, len(arr), value)

def _binary_search_iter(arr: List[int], l: int, r: int, value: int) -> Optional[int]:
    while l < r:
        m = (l + r) // 2 # floor (l + r) / 2
        if arr[m] < value:
            l = m + 1
        elif arr[m] > value:
            r = m - 1
        else:
            return m
    return None

def _binary_search_rec(arr:List[int], l: int, r: int, value: int) -> Optional[int]:
    if l >= r:
        return None
    m = (l + r) // 2 # floor (l + r) / 2
    if arr[m] < value:
        return _binary_search_rec(arr, m + 1, r, value)
    elif arr[m] > value:
        return _binary_search_rec(arr, l, m - 1, value)
    else:
        return m

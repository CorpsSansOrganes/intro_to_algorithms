from typing import List, Optional

def search(arr: List[int], key: int) -> Optional[int]:
    return _binary_search_iter(arr, 0, len(arr), key)

def _binary_search_iter(arr: List[int], l: int, r: int, key: int) -> Optional[int]:
    while l < r:
        m = (l + r) // 2 # floor (l + r) / 2
        if arr[m] < key:
            l = m + 1
        elif arr[m] > key:
            r = m 
        else:
            return m
    return None

def _binary_search_rec(arr:List[int], l: int, r: int, key: int) -> Optional[int]:
    if l >= r:
        return None
    m = (l + r) // 2 # floor (l + r) / 2
    if arr[m] < key:
        return _binary_search_rec(arr, m + 1, r, key)
    elif arr[m] > key:
        return _binary_search_rec(arr, l, m, key)
    else:
        return m

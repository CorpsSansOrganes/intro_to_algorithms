from typing import List

def find_min(arr: List[int]) -> int:
    min = arr[0]
    for e in arr[1:]:
        if e < min:
            min = e
    return min

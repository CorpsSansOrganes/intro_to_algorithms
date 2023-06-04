from typing import List

def find_max(arr: List[int]) -> int:
    max = arr[0]
    for e in arr[1:]:
        if e > max:
            max = e
    return max

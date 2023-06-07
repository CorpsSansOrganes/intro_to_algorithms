from typing import List 
from itertools import accumulate
def sort(arr: List[int]) -> List[int]:
    if not arr:
        return arr
    #return counting_sort(arr, max(arr))
    return counting_sort_w_negatives(arr, min(arr), max(arr))

def counting_sort(arr: List[int], k: int) -> List[int]:
    res = [0] * len(arr)
    count = [0] * (k + 1)

    for a in arr:
        count[a] += 1
    count = list(accumulate(count))
    
    for a in reversed(arr):
        count[a] -= 1
        res[count[a]] = a 
    
    return res

def counting_sort_w_negatives(arr: List[int], m: int, k: int) -> List[int]:
    res = [0] * len(arr)
    offset = -1 * m 
    count = [0] * (k + offset + 1)

    for a in arr:
        count[a + offset] += 1
    count = list(accumulate(count))

    for a in reversed(arr):
        count[a + offset] -= 1
        res[count[a + offset]] = a
    
    return res

A = [5, 4, 2, 3]
print(sort(A))

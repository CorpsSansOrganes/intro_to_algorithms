from typing import List 
from itertools import accumulate
def sort(arr: List[int]) -> List[int]:
    return counting_sort(arr, max(arr))

def counting_sort(arr: List[int], k: int) -> List[int]:
    res = [0] * len(arr)
    count = [0] * k 

    for a in arr:
        count[a] += 1
    count = list(accumulate(count))
    
    for a in reversed(arr):
        res[count[a]] = a 
        count[a] -= 1
    
    return res

from typing import List
from itertools import accumulate

def sort(arr: List[int]) -> List[int]:
    if not arr:
        return arr
    d = len(str(max(arr)))
    return radix_sort(arr, d)

def radix_sort(arr: List[int], d: int) -> List[int]:
    place = 1
    for _ in range(d):
        _counting_sort(arr, place)
        print(arr)
        place *= 10
    
    return arr 

def _counting_sort(arr: List[int], place: int): 
    res = [0] * len(arr)
    count = [0] * 10

    for a in arr:
        count[_get_digit(a, place)] += 1
    count = list(accumulate(count))

    for a in reversed(arr):
        count[_get_digit(a, place)] -= 1
        res[count[_get_digit(a, place)]] = a 

    arr[:] = res

def _get_digit(num: int, place: int) -> int:
    return (num // place) % 10

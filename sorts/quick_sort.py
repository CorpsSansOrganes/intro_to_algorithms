from typing import List

def sort(arr: List[int]) -> List[int]:
    temp = list(arr)
    quick_sort(temp, 0, len(temp))
    return temp

def quick_sort(arr: List[int], l: int, r: int):
    pass

def _partition(arr: List[int], l: int, r: int):
    pass

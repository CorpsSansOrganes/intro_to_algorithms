from typing import List

def sort(arr: List[int]) -> List[int]:
    for i in range(len(arr) - 1):
        print(arr)
        min_index = min(range(i, len(arr)), key=lambda j: arr[j])
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr

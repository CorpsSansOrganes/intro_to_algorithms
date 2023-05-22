from typing import List 
def merge_sort(arr: List[int], left: int = 0, right: int = None):
    '''
    Assumption: for each e in arr, e < 2^63 - 1
    '''
    if right is None:
        right = len(arr)

    if left >= right - 1:
        return 

    middle = (left + right) // 2 # discard decimal part
    merge_sort(arr, left, middle) 
    merge_sort(arr, middle, right)
    _merge(arr, left, middle, right)

def _merge(arr: List[int], left: int, middle: int, right: int):
    n1 = middle - left
    n2 = right - middle
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    # Copy left & right subarrays into temporary arrays
    for i in range(middle - left):
        L[i] = arr[left + i]
    L[n1] = 2**63 - 1

    for i in range(right - middle):
        R[i] = arr[middle + i]
    R[n2] = 2**63 - 1
    
    # Merging into arr
    r_i = 0
    l_i = 0
    for i in range(left, right):
        if L[l_i] <= R[r_i]:
            arr[i] = L[l_i]
            l_i += 1
        else:
            arr[i] = R[r_i]
            r_i += 1

A = [1, 5, 3]
print(f"Before: {A}")

merge_sort(A)
print(f"After: {A}")


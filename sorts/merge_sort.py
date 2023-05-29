from typing import List 

def sort(arr: List[int]) -> List[int]:
    temp: List[int] = list(arr)
    merge_sort(temp, 0, len(temp))
    return temp 

def merge_sort(arr: List[int], left: int = 0, right: int = None):
    if right is None:
        right = len(arr)

    if left >= right - 1:
        return 

    middle = (left + right) // 2 # discard decimal part
    merge_sort(arr, left, middle) 
    merge_sort(arr, middle, right)
    #_merge_with_infinity(arr, left, middle, right)
    _merge(arr, left, middle, right)

def _merge(arr: List[int], left: int, middle: int, right: int):
    '''
    Merge() subroutine following Cormen et al. 4nd Edition pseudocode.
    '''
    n1 = middle - left
    n2 = right - middle 
    L = [0] * n1 
    R = [0] * n2 

    # Copy arr[l..m) to L and arr[m...r) to R
    i = 0
    while i < n1 and i < n2:
        L[i] = arr[left + i]
        R[i] = arr[middle + i]
        i += 1
    while i < n1:
        L[i] = arr[left + i]
        i += 1
    while i < n2:
        R[i] = arr[middle + i]
        i += 1

    print(f"L= {L}")
    print(f"R= {R}")

    # Merge L & R in arr
    i = left
    i_l = 0
    i_r = 0
    while i_l < n1 and i_r < n2:
        if L[i_l] < R[i_r]:
            arr[i] = L[i_l]
            i_l += 1
        else:
            arr[i] = R[i_r]
            i_r += 1
        i += 1

    while i_l < n1:
        arr[i] = L[i_l]
        i_l += 1
        i += 1

    while i_r < n2:
        arr[i] = R[i_r]
        i_r += 1
        i += 1

print(sort([2,1,3]))

def _merge_with_infinity(arr: List[int], left: int, middle: int, right: int):
    '''
    Merge() subroutine using infinity elements as upper bounds on
    the subarrays ranges, as Cormen et al. 2nd Edition pseudocode
    shows.

    Assumption: for each e in arr, e < 2^63 - 1
    '''
    n1 = middle - left
    n2 = right - middle
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    # Copy left & right subarrays into temporary arrays
    for i in range(n1):
        L[i] = arr[left + i]
    L[n1] = 2**63 - 1 # placeholder for infinitly large value.

    for i in range(n2):
        R[i] = arr[middle + i]
    R[n2] = 2**63 - 1 # placeholder for infinitly large value.
    
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

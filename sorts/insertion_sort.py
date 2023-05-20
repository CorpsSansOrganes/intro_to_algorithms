from typing import List
def sort(arr: List[int]) -> List[int]:
    for i in range(1, len(arr)):
        key = arr[i]
        pos = i - 1
        while pos > -1 and arr[pos] > key:
            arr[pos + 1] = arr[pos]
            pos -= 1
        arr[pos + 1] = key
    return arr

if __name__ == "__main__":
    print(sort([5, 4, 3, 2, 1]))

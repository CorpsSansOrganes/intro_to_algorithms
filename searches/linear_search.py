from typing import List, Optional

def search(arr: List[int], value: int) -> Optional[int]:
    found = [i for i, e in enumerate(arr) if e == value]
    print(found)

if __name__ == "__main__":
    search([1, 2, 3], 1)
    search([1, 2, 3], 2)
    search([1, 2, 3], 4)
    search([1, 2, 2, 3], 2)

from typing import List, Optional

def search(arr: List[int], value: int) -> Optional[int]:
    for i, e in enumerate(arr):
        if e == value:
            return i 
    return None

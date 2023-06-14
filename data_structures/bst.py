class node:
    def __init__(self, value: int,
                 l: 'node' = None,
                 r: 'node' = None,
                 p: 'node' = None) -> None:
        self.value = value 
        self.l = l 
        self.r = r 
        self.p = p
    
    def set_right(self, r: 'node') -> None:
        self.r = r

    def set_left(self, l: 'node') -> None:
        self.l = l 

    def set_parent(self, p: 'node') -> None:
        self.p = p 

class bst:
    def __init__(self, root: 'node') -> None:
        self.root = root

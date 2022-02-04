import random
class Solution:
    
    def __init__(self, w: list[int]):
        self.w = w
        self.options = list(range(0, len(w)))
            

    def pickIndex(self) -> int:
        return random.choices(self.options, weights=self.w)[0]
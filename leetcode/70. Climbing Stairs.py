class Solution:
    def __init__(self):
        self.store = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n in self.store:
            return self.store[n]
        else:
            self.store[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.store[n]

class Solution:
    def isHappy(self, n: int) -> bool:
        store = set()
        while n:
            if n in store:
                return False
            store.add(n)
            n = str(n).replace("0", "")
            n = list(n)
            n = sum(int(i)**2 for i in n)
            if n == 1:
                return True

class Solution:
    def queryString(self, S: str, N: int) -> bool:
        def Bin(n):
            if n == 0:
                return ""
            if n >= 1:
                return Bin(n//2) + str(n % 2)
        for i in range(1, N+1):
            if Bin(i) not in S:
                return False
        return True

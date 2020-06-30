class Solution:
    def reverse(self, x: int) -> int:
        remember = 0
        result = 0
        neg = False
        if x < 0:
            neg = True
            x = abs(x)
        while x != 0:
            remember = x % 10
            x = x // 10
            result = result * 10 + remember
        if result > 2**31:
            return 0
        return -result if neg else result

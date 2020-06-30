class Solution:
    def isPalindrome(self, x: int) -> bool:
        initial = x
        if x < 0:
            return 0
        result, remainder = 0, 0
        while x != 0:
            remainder = x % 10
            x = x // 10
            result = result * 10 + remainder
        return True if initial == result else False

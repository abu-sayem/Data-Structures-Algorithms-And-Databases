class Solution:
    def reverseString(self, s: List[str]) -> None:
        l = len(s)
        n = l // 2
        for i in range(n):
            s[i], s[l-i-1] = s[l-i-1], s[i]
        return s

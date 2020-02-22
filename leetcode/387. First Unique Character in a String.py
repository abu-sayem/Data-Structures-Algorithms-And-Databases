class Solution:
    def firstUniqChar(self, s: str) -> int:
        store = {}
        for i in s:
            if i in store:
                store[i] = store[i] + 1
            else:
                store[i] = 1
        for i, j in enumerate(s):
            if store[j] == 1:
                return i
        return -1

class Solution(object):
    def singleNumber(self, nums):
        store = set()
        for i in nums:
            if i in store:
                store.remove(i)
            else:
                store.add(i)
        return store.pop()

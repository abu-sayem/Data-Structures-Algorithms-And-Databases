class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        store, store2 = set(), set()
        count = 0
        for i in nums1:
            store.add(i)

        for i in nums2:
            if i in store and i not in store2:
                nums1[count] = i
                store2.add(i)
                count += 1
        return nums1[:count]

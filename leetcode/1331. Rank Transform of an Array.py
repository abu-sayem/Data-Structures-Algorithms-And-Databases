class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        store = {}
        new_list = list(arr)
        new_list.sort()
        count = 1
        for i, j in enumerate(new_list):
            if new_list[i-1] < new_list[i]:
                count += 1
            store[j] = count
        for i in range(len(arr)):
            new_list[i] = store[arr[i]]
        return new_list

#Solution 1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            temp = target - nums[i]
            for j in range(i+1, length):
                if nums[j] == temp:
                    return [i, j]

# Better solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        for i, num in enumerate(nums):
            temp = target - num
            if temp not in store:
                store[num] = i
            else:
                return [store[temp], i]

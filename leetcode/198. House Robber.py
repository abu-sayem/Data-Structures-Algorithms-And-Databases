class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        s = [0] * n
        s[0] = nums[0]
        s[1] = max(nums[0], nums[1])
        for i in range(2, n):
            s[i] = max((nums[i] + s[i-2]), s[i-1])
        return s[n-1]

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = len(nums)

        low, high = 0, l

        while(low < high):
            mid = low + (high-low) // 2
            if nums[mid] == target or nums[mid-1] < target < nums[mid]:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return high

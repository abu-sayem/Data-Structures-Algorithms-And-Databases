class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        bucket = [0] * 101
        for num in nums:
            bucket[num] += 1

        accu = [0] * 101
        for i in range(1, 101):
            accu[i] = accu[i-1] + bucket[i-1]

        return [accu[num] for num in nums]

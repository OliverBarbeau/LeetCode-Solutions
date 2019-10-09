class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        m = nums[0]
        maxEndingHere = m
        for i in range(1, len(nums)):
            maxEndingHere = max(nums[i], maxEndingHere + nums[i])
            m = max(m, maxEndingHere)
            
        return m
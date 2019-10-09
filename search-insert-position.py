class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lastNum = nums[0]
        if target <= lastNum:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == target or (lastNum < target and nums[i] > target):
                return i
            lastNum = nums[i]
        if target > nums[-1]:
            return len(nums)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        prior = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prior:
                nums[i] = '1'
            else:
                prior = nums[i]
        adj = 0
        for i in range(1, len(nums)):
            if nums[i] == '1':
                adj += 1
            else:
                nums[i-adj] = nums[i]
            
        return len(nums)-adj
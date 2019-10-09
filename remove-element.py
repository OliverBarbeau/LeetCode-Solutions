class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #scan list of ints:
        #when you find target move the position ahead of it to this position
        #loop keeping an adjustment variable that changes when you find the target
        #adjust = 0
        
        #for num in nums:
        #   if num == target:
        #       assign num to nums[index-adjust]
        adjustment = 0
        length = len(nums)
        for i in range(length):
            if nums[i] == val:
                adjustment += 1
            else:
                nums[i-adjustment] = nums[i]
        return length-adjustment
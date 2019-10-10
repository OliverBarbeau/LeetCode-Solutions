# Problem #238
# https://leetcode.com/problems/product-of-array-except-self
# Given an array nums of n integers where n > 1,  
# return an array output such that output[i] is equal to the product of 
# all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? 
# (The output array does not count as extra space for 
# the purpose of space complexity analysis.)

class Solution:
    def productExceptIndex(self, prod, nums, i):
        if i == len(nums):
            return 1
        else:
            rightProduct = self.productExceptIndex(prod*nums[i], nums, i+1)
            newNum = nums[i]
            nums[i] = prod * rightProduct
            return newNum * rightProduct
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        self.productExceptIndex(1, nums, 0)
        return nums 
            
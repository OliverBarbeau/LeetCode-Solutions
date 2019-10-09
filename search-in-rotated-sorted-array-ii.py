# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

# You are given a target value to search. If found in the array return true, otherwise return false.

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false



class Solution:
    def binarySearchForPivot(self,nums):
        if len(nums) == 0:
            return -1
        left = 0
        mid = 1
        while mid < len(nums) and nums[left] <= nums[mid]:
            left += 1
            mid += 1
        return mid % len(nums)
    def search(self, nums: List[int], target: int) -> bool:
        # hold aR and aL variables which track the left and right points
        # as if this were a regularly sorted list
        pivot = self.binarySearchForPivot(nums)
        print("Pivot amount:", pivot)
        length = len(nums)
        aL, aR = 0, length-1
        while aL <= aR:
            aMid = ( aL + aR ) // 2
            mid = ( aMid + pivot ) % length
            if nums[mid] == target:
                return True
            elif target <= nums[mid]:
                aR = aMid-1
            else:
                aL = aMid+1
        return False
    
# Problem #34
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        loc = -1
        lo, hi = 0, len(nums) - 1
        while lo <= hi and loc == -1:
            mid = (hi+lo)//2
            if nums[mid] == target:
                loc = mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        lo, hi = loc, loc
        while lo > 0 and nums[lo] == nums[lo-1]:
            lo -= 1
        while hi != -1 and hi < len(nums)-1 and nums[hi] == nums[hi+1]:
            hi += 1
        return [lo, hi]
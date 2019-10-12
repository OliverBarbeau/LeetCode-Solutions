# Problem #220 
# https://leetcode.com/problems/contains-duplicate-iii/
# Given an array of integers, find out whether there are two distinct indices
# i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t
# and the absolute difference between i and j is at most k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3, t = 0
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1, t = 2
# Output: true
# Example 3:

# Input: nums = [1,5,9,1,5,9], k = 2, t = 3
# Output: false


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        key = lambda x: x[0]
        newNums = []
        for i in range(len(nums)):
            newNums.append((nums[i], i))
            
        newNums = sorted(newNums, key=key)
        print(newNums)
        m = 0
        l = 1
        while m < len(newNums)-1:
            print(newNums[m])
            while l < len(newNums) and newNums[l][0] - newNums[m][0] <= t:
                if abs(newNums[l][1]-newNums[m][1]) <= k:
                    return True
                l += 1
            m += 1
            l = m+1
        return False
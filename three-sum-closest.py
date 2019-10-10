# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

# Example:

# Given array nums = [-1, 2, 1, -4], and target = 1.

# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution:
    def threeSumClosest(self, nums: List[int], target) -> List[List[int]]:
        sols = []
        nums = sorted(nums)
        l = len(nums)
        i = 0
        closestDist = float('inf')
        closest = 0
        while i < l:
            if (i != 0 and nums[i] != nums[i-1]) or i == 0:
                inverse = target-nums[i]
                j = i+1
                k = l-1
                while j < k:
                    checkSum = nums[j] + nums[k]

                    dist = abs(inverse-checkSum)
                    if dist < closestDist:
                        closest = nums[i] + checkSum
                        closestDist = dist
                    if checkSum > inverse:
                        k-=1
                        while j < k and nums[k] == nums[k+1]:
                            k-=1
                    else:
                        j += 1
                        while j < k and nums[j] == nums[j-1]:
                            j+=1
            i +=1 
        return closest
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution:
    def threeSum(self, arr, target = 0):
        results = []
        #take first number, search for 2 sum that equals its compliment past this one
        arr = sorted(arr)
        for f in range(len(arr)-2):
            if f == 0 or arr[f] > arr[f-1]:
                s = f+1
                t = len(arr)-1
                while s < t:
                    thisSum = arr[f]+arr[s]+arr[t]
                    if thisSum == target:
                        results.append([arr[f],arr[s],arr[t]])
                        curS = s
                        while s < t and arr[s] == arr[curS]:
                            s+=1
                    elif thisSum < target:
                        curS = s                        
                        while s < t and arr[s] == arr[curS]:
                            s+=1
                    else:
                        curT = t
                        while s < t and arr[t] == arr[curT]:
                            t-=1
        return results
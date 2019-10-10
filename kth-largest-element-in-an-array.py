# Problem #215
# https://leetcode.com/problems/kth-largest-element-in-an-array
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Example 1:

# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# Example 2:

# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.


#Concise pythonic soluion
# class Solution:
#     def findKthLargest(self, nums, k):
#         return sorted(nums)[-k]


import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        kEls = []
        for num in nums:
            print(num)
            if len(kEls) == k:
                if num > kEls[0]:
                    removed = heapq.heappop(kEls)
                    print("removed item:", removed)
                    heapq.heappush(kEls, num)
                    print("pushed", num)
                    #heapq.heapify(kEls)
            else:
                print("heap not long enough, adding:", num)
                heapq.heappush(kEls, num)
                #heapq.heapify(kEls)
        print("kEls", kEls)
        
        return kEls[0]



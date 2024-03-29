# Problem #69
# https://leetcode.com/problems/sqrtx
# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# Example 1:

# Input: 4
# Output: 2
# Example 2:

# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        #search for sqrt
        lo = 1

        hi = x // 2
        mid = (hi+1) // 2
        
        1 ,2,3, 4 ,5,6,7,8,(9)
        while lo < hi:
            mid = (hi+lo) // 2
            if (mid * mid) <= x and ((mid+1) * (mid+1)) > x:
                return mid
            elif mid * mid < x:
                lo = mid+1
                mid = hi
                
            else:
                hi = mid-1
                mid = lo
                
        return mid
# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store 
# integers within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x):
        signed = False
        if x < 0:
            signed = True
            x = -x
        num = 0
        while (x != 0):
            num *= 10
            num = int(num + (x % 10))
            x = int(x / 10)
        if (abs(num) > (1 << 31) - 1):
            return 0
        if (signed):
            return -1*num
        else:
            return num
// Problem #231
// https://leetcode.com/problems/power-of-two
//# Given an integer, write a function to determine if it is a power of two.

// # Example 1:

// # Input: 1
// # Output: true 
// # Explanation: 20 = 1
// # Example 2:

// # Input: 16
// # Output: true
// # Explanation: 24 = 16
// # Example 3:

// # Input: 218
// # Output: false

class Solution {
    public boolean isPowerOfTwo(int n) {
        int prior = 0;
        int myTwo = 1;
        while (myTwo < n && myTwo > prior){
            prior = myTwo;
            myTwo = myTwo << 1;
        }
        if (n == myTwo){
            return true;
        }
        return false;
    }
}
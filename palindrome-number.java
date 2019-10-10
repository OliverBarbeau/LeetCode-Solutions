// Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

// Example 1:

// Input: 121
// Output: true
// Example 2:

// Input: -121
// Output: false
// Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
// Example 3:

// Input: 10
// Output: false
// Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
// Follow up:

// Coud you solve it without converting the integer to a string?

class Solution {
    public boolean isPalindrome(int x) {
        //use mod 10 to grab last digit
        //how do you simultaniously grab first digit
        if (x < 0){
            return false;
        }
        int copy = x;
        int lastPos = 0;
        int[] digits = new int[10];
        while (copy >= 10){
            digits[lastPos] = copy % 10;
            lastPos += 1;
            copy /= 10;
        }
        digits[lastPos] = copy % 10;
        
        int limit = lastPos / 2;
        for (int i = 0; i <= limit; i++){
            if (digits[i] != digits[lastPos-i]){
                return false;
            }
        }
        return true;
    }
    
}
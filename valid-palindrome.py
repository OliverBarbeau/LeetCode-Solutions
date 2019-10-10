# Problem #125
# https://leetcode.com/problems/valid-palindrome
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for char in s:
            if char.isalnum():
                newS += char.lower()
        check1 = len(newS)-1
        if check1 == -1 or check1 == 0:
            return True
        print(check1)
        check2 = ((check1) % 2)
        check1 = check1 // 2
        check2 += check1
        print(check1,check2)
        while check1 >= 0 and newS[check1] == newS[check2]:
            print(check1, check2)
            check1-=1
            check2+=1
        if check1 == -1:
            return True
        return False
            
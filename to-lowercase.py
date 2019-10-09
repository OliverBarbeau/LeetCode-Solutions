# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

# Example 1:

# Input: "Hello"
# Output: "hello"
# Example 2:

# Input: "here"
# Output: "here"
# Example 3:

# Input: "LOVELY"
# Output: "lovely"

class Solution:
    def toLowerCase(self, str: str) -> str:
        newStr = ""
        for char in str:
            ordo = ord(char)
            if ordo < 91 and ordo >= 65:
                newStr += chr(ordo+32)
            else:
                newStr += char
        return newStr
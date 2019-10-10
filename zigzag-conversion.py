# Problem #6
# https://leetcode.com/problems/zigzag-conversion
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:

# P     I    N
# A   L S  I G
# Y A   H R
# P     I

class Solution:
    def convert(self, s, numRows):
        
        
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        rows = []
        i = 0
        while i < numRows:
            rows.append("")
            i += 1
        rev = True
        curRow = 0
        high = numRows - 1
        for char in s:
            rows[curRow] += char
            if curRow == 0 or curRow == high:
                rev = not rev
            
            if rev:
                curRow -= 1
            else:
                curRow += 1
        rStr = ''
        for row in rows:
            rStr += row
        return rStr
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

# Example 1:

# Input: 3
# Output: "III"
# Example 2:

# Input: 4
# Output: "IV"
# Example 3:

# Input: 9
# Output: "IX"
# Example 4:

# Input: 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.
# Example 5:

# Input: 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ""
        #get M's
        fig = num // 1000
        if fig > 0:
            num = num % (1000*fig)
            for _ in range(fig):
                roman += "M"
        fig = num // 100
        if fig > 0:
            num = num % (100*fig)
            if fig == 4:
                roman += "CD"
            elif fig == 9:
                roman += "CM"
            else:
                if fig >= 5:
                    roman += "D"
                    fig -= 5
                while fig > 0:
                    roman += "C"
                    fig -= 1
        
        fig = num // 10
        if fig > 0:
            num = num % (10*fig)
            if fig == 4:
                roman += "XL"
            elif fig == 9:
                roman += "XC"
            else:
                if fig >= 5:
                    roman += "L"
                    fig -= 5
                while fig > 0:
                    roman += "X"
                    fig -= 1
        if num == 4:
            roman += "IV"
        elif num == 9:
            roman += "IX"
        else:
            if num >= 5:
                roman += "V"
                num -= 5
            while num > 0:
                roman += "I"
                num -= 1
        return roman
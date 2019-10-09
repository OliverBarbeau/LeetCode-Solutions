class Solution:
    def romanToInt(self, s: str) -> int:
        digits = {"I":1,"V":5, "X":10,"L":50,"C":100,"D":500,"M":1000}
        digit = "I"
        inty = 0
        for strInd in range(len(s)-1, -1,-1):
            if s[strInd] == digit:
                inty += digits[digit]
            elif digits[s[strInd]] > digits[digit]:
                inty += digits[s[strInd]]
                digit = s[strInd]
            elif digits[s[strInd]] < digits[digit]:
                inty -= digits[s[strInd]]
        return inty
                
class Solution:
    def getPalidromeLength(self, s, i):
        length = 1
        if i >= len(s):
            return s[0]
        else:
            #is center two or one letters?
            j = i-1
            k = i+2
            l = 2
            if i+1 < len(s) and s[i] == s[i+1]:
                print("double Center")
                while j >= 0 and k < len(s) and s[j] == s[k]:
                    j = j-1
                    k = k+1
                    l = l+2
                length = l
            oldJ = j
            j = i-1
            k = i+1
            l = 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                    j = j-1
                    k = k+1
                    l = l+2
            return (max(length, l),min(j+1, oldJ+1))
            
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or len(s) == 0:
            return s
        maxPalStringIndex = 0
        maxLength = 0
        center = len(s)//2
        i = center
        spacing = 0
        while i >= 0 and i < len(s):
            print('here')
            l, start = self.getPalidromeLength(s,i)
            if l > maxLength or (l == maxLength and start <= maxPalStringIndex):
                maxLength = l
                maxPalStringIndex = start
            if spacing >= 0:
                spacing = spacing*-1 -1
            else:
                spacing = spacing*-1
            i = center + spacing
        return s[maxPalStringIndex : maxPalStringIndex+maxLength]
        #check if index is center of palidrome
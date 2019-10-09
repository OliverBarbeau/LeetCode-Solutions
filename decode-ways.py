# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.

# Example 1:

# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

class Solution:
    decodings = {} #encoded with start position of this string
    def numDecodings(self, s, i=0):
        
        if i == 0:
            self.decodings = {}
        if i in self.decodings:
            return self.decodings[i]
        l = len(s)
        if l-1 == i:
            
            self.decodings[i] = 1
            print("add ", s[i])

            return 1
        elif i == l:
            self.decodings[i] = 1
            return 1
        else:
            if s[i] == "1":
                result = self.numDecodings(s, i+1) + self.numDecodings(s, i+2)
                print("add ", s[i:i+2], "and ", s[i])
            elif s[i] == "2":
                if int(s[i+1]) <= 6:
                    result = self.numDecodings(s, i+1) + self.numDecodings(s, i+2)
                    print("add ", s[i:i+2], "and ", s[i])
                

                else:
                    result =  self.numDecodings(s, i+1)
                    print("add ", s[i])
            elif s[i] != "0":
                result = self.numDecodings(s, i+1)

                print("add ", s[i])

            else:
                #string @ i is 0
                result = 0
                print("do not add ", s[i])

            self.decodings[i] = result
            return result
                
        
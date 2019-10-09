import heapq
class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        #keep set of characters in current working string
        #track index of last start of the working string
        #when we find a character already in our set we simply re calculate max
        # on the currentIndex - startIndex and reassign our max, if necessary
        
        Q = []
        charDict = {}
        maxLen = 0
        start = 0
        for i in range(len(s)):
            if s[i] in charDict:
                #print("start is:", start)
                #we've seen this before
                #calculate substring length
                
                #print("seen char before:", s[i])
                pops = charDict[s[i]] - start
                for j in range(pops):
                    char = Q[0]
                    #print("popping char", char)
                    Q = Q[1:]
                    del charDict[char]
                char = Q[0]
                Q = Q[1:]
                Q.append(char)
                start = charDict[char] + 1
                #print("new start is", start)
                charDict[char] = i
                #print("charDict at", char, "is now", i)
                #reassign start index to index after the last occurance of this character
                
                #remove 
            else:
                
                char = s[i]
                #print("adding new char:", char)
                charDict[char] = i
                Q.append(char)
                #print("charDict at", char, "is now", i)
                
                
            l = len(Q)
            #print("length of Q is:", l, "\n Q looks like:", Q)
            #reassign max accordingly
            maxLen = max(l, maxLen)
        return maxLen
            
import string
#start: 1:36PM 10/8/2019
class Solution:
    letterToPrime = {}
    primes = "2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103"
    primes = primes.split(", ")
    letters = string.ascii_lowercase
    for i in range(26):
        letterToPrime[letters[i]] = int(primes[i])
    
    def hashAString(self, s):
        prod = 1
        for char in s:
            prod *= self.letterToPrime[char]
        return prod
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringHashToWordList = {}
        for word in strs:
            h = self.hashAString(word)
            if h in stringHashToWordList:
                stringHashToWordList[h] = stringHashToWordList[h] + [word]
            else:
                stringHashToWordList[h] = [word]
        rList = []
        for key, val in stringHashToWordList.items():
            rList.append(val)
        return rList

#end: 1:47PM 10/8/2019
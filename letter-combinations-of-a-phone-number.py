# Problem #17
# https://leetcode.com/problems/letter-combinations-of-a-phone-number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution:
    map = {2:['a','b','c'], 3: ['d','e','f'], 4: ['g','h','i'], 5: ['j','k','l'], 6: ['m','n','o'], 7: ['p','q','r','s'],8: ['t','u','v'], 9: ['w','x','y','z']}
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 1:
            return self.map[int(digits[0])]
        elif len(digits) == 0:
            return []
        combinations = self.letterCombinations(digits[1:])
        newCombinations = []
        for combo in combinations:
            for char in self.map[int(digits[0])]:
            
                newCombinations.append(char+combo)
        return newCombinations
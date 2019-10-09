MAP = {'2':['a', 'b', 'c'], '3': ['d','e','f'], '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'], '7': ['p','q','r', 's'], '8': ['t','u','v'], '9': ['w','x','y','z']}

class Solution:
    sols = []
    def generateSolution(self, digits, sol):
        if digits == []:
            if sol:
                self.sols.append(sol)
            return
        digit = digits.pop()
        for letter in MAP[digit]:
            self.generateSolution(digits[::], letter+sol)
        
            
    def letterCombinations(self, digits: str) -> List[str]:
        self.sols = []
        digits = list(digits)
        self.generateSolution(digits, "")
        return self.sols
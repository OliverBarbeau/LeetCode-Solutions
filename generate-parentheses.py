# Problem #22
# https://leetcode.com/problems/generate-parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given n = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
class Solution:
    sols = []
    def generateSolution(self, n: int, openParens: int, sol: str) -> str:
            if n == 0 and openParens == 0:
                self.sols.append(sol)
            if openParens:
                self.generateSolution(n, openParens-1, sol + ")" )
            if n:
                self.generateSolution(n-1, openParens+1, sol + "(" )
            
    def generateParenthesis(self, n: int) -> List[str]:
        self.sols = []
        emp = ""
        self.generateSolution(n,0,emp)        
        return self.sols[::-1]

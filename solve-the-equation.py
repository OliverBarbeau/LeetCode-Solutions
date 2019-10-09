# Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.

# If there is no solution for the equation, return "No solution".

# If there are infinite solutions for the equation, return "Infinite solutions".

# If there is exactly one solution for the equation, we ensure that the value of x is an integer.

# Example 1:
# Input: "x+5-3+x=6+x-2"
# Output: "x=2"
# Example 2:
# Input: "x=x"
# Output: "Infinite solutions"
# Example 3:
# Input: "2x=x"
# Output: "x=0"
# Example 4:
# Input: "2x+3x-6x=x+2"
# Output: "x=-1"
# Example 5:
# Input: "x=x+2"
# Output: "No solution"

class Solution:
    def parseExp(self,exp):
        #define set of digits for parsing
        digits = set(['1','2','3','4','5','6','7','8','9','0'])
        
        value = 0
        coef = 0
        #move through the string over each element once starting at the end
        i = len(exp)-1
        while i >= 0:
            j = i-1
            #character is a digit, so we build out the digit checking the indecies before it
            if exp[i] in digits:
                digit = exp[i]
                while j >= 0 and exp[j] in digits:
                    digit = exp[j] + digit
                    j = j-1
                #check for sign of parsed value and add to this expression's total value
                if j >= 0 and exp[j] == "-":
                    value -= int(digit)
                else:
                    value += int(digit)
            #character is x, so we build a digit in a similar way as above
            elif exp[i] == 'x':
                digit = ""
                while j >= 0 and exp[j] in digits:
                    digit = exp[j] + digit
                    j = j-1

                if digit == "":
                    digit = "1"
                #check for sign of parsed coeficient and add it to this expression's total coef

                if j >= 0 and exp[j] == "-":
                    coef -= int(digit)
                else:

                    coef += int(digit)
            i = j-1
        return (coef,value)
    
    
    
    
    def solveEquation(self, equation: str) -> str:
        
        #seperate expressions from either side of the equation
        expressions = equation.split("=")
        expA = self.parseExp(expressions[0])
        expB = self.parseExp(expressions[1])
        #balance expressions
        x = expA[0]-expB[0]
        v = expB[1]-expA[1]
        if x == 0:
            if v == 0:
                
                return "Infinite solutions"
            return "No solution"
        return "x="+str(v//x)
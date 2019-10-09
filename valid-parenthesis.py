class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        for char in s:
            if char == "(":
                stack.append(")")
            elif char == "{":
                stack.append("}")
            elif char == "[":
                stack.append("]")
            else:
                if len(stack) == 0:
                    return False
                el = stack.pop()
                if el != char:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
                
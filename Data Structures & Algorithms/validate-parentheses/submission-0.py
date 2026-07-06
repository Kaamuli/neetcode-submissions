class Solution:
    def isValid(self, s: str) -> bool:
        bracket_combo = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        bracket_stack = [] #Will store brackets 
        for bracket in s:
            if bracket not in bracket_combo:
                bracket_stack.append(bracket)
            elif bracket_combo[bracket] not in bracket_stack:
                return False
            elif bracket_stack[-1] == bracket_combo[bracket]:
                bracket_stack.pop()
        
        print(bracket_stack)
        if bracket_stack:
            return False
        else:
            return True
            
            

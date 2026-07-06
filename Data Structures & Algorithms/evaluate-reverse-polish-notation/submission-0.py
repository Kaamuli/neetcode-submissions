class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = set({"+","-","*","/"}) #Stores the different operations

        stack = [] #Store our numbers and eventually our output 

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                b = stack.pop()
                a = stack.pop()

                if tokens[i] == "+":
                    stack.append(a+b)
                elif tokens[i] == "-":
                    stack.append(a-b)
                elif tokens[i] == "/":
                    stack.append(int(a/b))
                elif tokens[i] == "*":
                    stack.append(a*b)
        return stack[-1]

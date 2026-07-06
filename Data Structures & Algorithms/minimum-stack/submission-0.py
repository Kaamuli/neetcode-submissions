class MinStack:

    def __init__(self):
        self.stack = []
        self.min_values = [] #store as an array, with top value being most recent minimum value

    def push(self, value: int) -> None:
        self.stack.append(value)
    
        if self.min_values:
            if value < self.min_values[-1]: 
                self.min_values.append(value)
            else:
                self.min_values.append(self.min_values[-1])
        else:
            self.min_values.append(value)

    def pop(self) -> None:

        self.stack.pop()
        self.min_values.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        output = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and (temperatures[i] > stack[-1][0]):
                output[stack[-1][1]] = i - stack[-1][1]
                stack.pop()
            stack.append((temperatures[i],i))
        return output

            
            
        
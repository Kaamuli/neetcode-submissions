class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #Keep track of temperatures [temp, index]
        output = [0 for i in range(len(temperatures))] #Initialise output array with 0's

        
        for i,temp in enumerate(temperatures): #Store the index, temperature of array
            if not stack:
                stack.append([temp,i])
            elif temp < stack[-1][0]:
                stack.append([temp,i])
            else:
                while stack and temp > stack[-1][0]:
                    popped_temp, index = stack.pop()
                    output[index] = i - index
                stack.append([temp,i])
        
        return output
                

                    

            
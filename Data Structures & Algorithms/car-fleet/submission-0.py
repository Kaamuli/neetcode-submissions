class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position = [target - pos for pos in position] #relative position
        
        time = [position[i]/speed[i] for i in range(len(position))]

        car = [] #Store the time: relative position
        stack = [] #Store the slowest time?
        output = 0 #store the fleet count
        for i in range(len(position)):
            car.append([position[i],time[i]]) #store car pos and speed in a combined array
        
        car.sort()

        minimum_time = car[0][1]

        print(car)


        for i in range(len(position)):
            if len(position) == 1:
                minimum_time = car[0][1]
                return len(position)
            elif i == len(position) - 1:
                stack.append(car[i][1])
            elif car[i+1][1] <= minimum_time:
                minimum_time = max(minimum_time,car[i+1][1])
                stack.append(minimum_time)
            elif car[i+1][1] > minimum_time:
                while stack:
                    stack.pop()
                output += 1
                minimum_time = max(minimum_time,car[i+1][1])
                stack.append(minimum_time)
        
        if stack:
            output += 1

        return output
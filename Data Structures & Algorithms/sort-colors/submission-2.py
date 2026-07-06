class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3 #Count array to store with index 0,1,2 to tally the counts
        for num in nums:
            count[num] += 1
        
        index = 0 
        num = 0

        for i in range(3): #Loop through each array element count
            while count[i] != 0:
                count[i] -= 1 
                nums[index] = i
                index += 1

            

        
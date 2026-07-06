class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = []
        suffix_array = []
        answer_array = []

        #To build left array

        for i in range(len(nums)):
            if i == 0:
                prefix_array.append(1)
                suffix_array.append(1)
            else:
                prefix_array.append(nums[i-1] * prefix_array[i-1])
                suffix_array.append(nums[len(nums) - i] * suffix_array[i-1]) #To traverse opposite direction you thought it, just NO IMPLEMENTATION (relied on ai a bit to much to figure out imo)
        
        suffix_array.reverse() #So that things align

        for i in range(len(nums)):
            answer_array.append(prefix_array[i] * suffix_array[i])
        
        return answer_array


    


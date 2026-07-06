class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Intialise a hashmap for storing the index/nums we've seen
        num_hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num #The complement is value we're looking for to get our target
            
            if complement in num_hashmap:
                return [num_hashmap[complement], i]
            num_hashmap[num] = i #If number isn't already in hashmap it adds it

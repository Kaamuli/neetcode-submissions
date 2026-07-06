class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #hashset = set() #Will contain the array but can access in O(1) lookup

        hashset = set(nums)
        
        longest = 0
        length = 0

        for num in hashset: #Was looping through nums before should do it here as O(1) time!
            #Check if its the start of a sequence
            i = 0 #iterator to loop through nums
            if num - 1 not in hashset:
                #Loop through to get to end of loop
                while i < len(nums):
                    if num + i in hashset:
                        length += 1
                    else:
                        break
                    i += 1
                longest = max(length, longest)
                length = 0
        
        return longest
           

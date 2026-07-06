class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        hashmap = {} #empty hash
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1

                if hashmap[num] > n/2:
                    return num
            else:
                hashmap[num] = 1
                
                if hashmap[num] > n/2:
                    return num
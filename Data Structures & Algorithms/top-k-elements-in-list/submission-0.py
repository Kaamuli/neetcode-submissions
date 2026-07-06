class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countOfnums = {} #Hashmap for storing counts and respective number
        freq = [[] for i in range(len(nums) + 1)] #Creates an array of empty lists the same size as array of nums as this is the max times number can repeat itself
        k_count = 0 #This is a value to compare to k to ensure we have the k most frequent elements
        most_freq_elements = [] #array to store final answer
        for num in nums:
            if num in countOfnums:
                countOfnums[num] += 1
            else:
                countOfnums[num] = 1
        for num, count in countOfnums.items():
            freq[count].append(num) #at the index corresponding to the count, append the number!
        
        for countList in reversed(freq):
            if countList: #check if list is empty
                for num in countList:
                    most_freq_elements.append(num)
                if len(most_freq_elements) == k:
                    return most_freq_elements
                
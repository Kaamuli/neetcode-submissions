class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
     num_counts = {} #Hashmap to store the numbers and corresponding counts
     frequency_count = [[] for i in range(len(nums)+1)] #An array where the index is the count and the value is the list of numbers equal to that count.
     output = [] #This will store the array of top k frequent elements
     counter = 0 #This will store what number of frequent elements we have

     for num in nums: #Count to keep track of the elements used and there counts
        if num not in num_counts:
            num_counts[num] = 1
        else:
            num_counts[num] += 1
     
     for value,count in num_counts.items(): #This builds out the array
        frequency_count[count].append(value)
     print(frequency_count)

     for count in reversed(frequency_count):
        if count: #Note that the count is an array of values equal to that count!
            for item in count:
                if counter < k:
                    output.append(item)
                    counter += 1
     return output


    
        
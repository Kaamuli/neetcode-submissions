class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #hashset = set() #Will contain the array but can access in O(1) lookup

        hashset = set(nums)

        #for num in nums:
            #if num in hashet: #Dont need to handle duplicates sets do that already
                #continue
            #else:
                #hashset.add(num) #Achieve O(1) lookup!

        sequences = [] #Will hold list of sequences

        current_seq = []
        for num in nums:
            #Check if its the start of a sequence
            if num - 1 not in hashset:
                #Loop through to get to end of loop
                for i in range(len(nums)):
                    if num + i in  hashset:
                        current_seq.append(num + i)
                    else:
                        break
            sequences.append(current_seq)
            current_seq = []
        
        longest_conseq_seq = max((len(sequence) for sequence in sequences), default = 0)
        
        return longest_conseq_seq

           

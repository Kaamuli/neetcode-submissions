class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} #This will store the output with the list of lists of anagrams

        for word in strs:
            #Create a seperate character count for each word
            char_count = [0] * 26

            for letter in word:

                char_count[ord(letter) - ord('a')] += 1 #Adds a +1 to each letter that appears and stores it in array

            char_count = tuple(char_count) #Converts array to tuple as cannot have a mutable key...

            #Check if char_count is NOT in anagrams already
            if char_count not in anagrams:
                anagrams[char_count] = []
            
            anagrams[char_count].append(word) #Adds word to each count it can be broken up into
        return list(anagrams.values())
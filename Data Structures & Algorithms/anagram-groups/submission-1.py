class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} #hashmap to store the group anagrams

        for word in strs:

            #Initialise a char count for each word
            char_count = [0] * 26

            for letter in word:

                char_count[ord(letter) - ord("a")] += 1 #Increments each character by 1 relative to position in alphabet

            char_count = tuple(char_count)

            #Check if char count is NOT already in anagrams hashmap
            if char_count not in anagrams:
                anagrams[char_count] = []
            
            anagrams[char_count].append(word) #Adds to char_count
        return list(anagrams.values())
            

            
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer1 = 0
        pointer2 = 0
        merged_array = []

        if len(word1) < len(word2):
            char_match_length = 0
            while char_match_length < len(word1):
                merged_array.append(word1[pointer1])
                pointer1 += 1
                merged_array.append(word2[pointer2])
                pointer2 += 1
                char_match_length += 1
            for i in range(char_match_length, len(word2)):
                merged_array.append(word2[pointer2])
                pointer2 += 1

        if len(word1) > len(word2):
            char_match_length = 0
            while char_match_length < len(word2):
                merged_array.append(word1[pointer1])
                pointer1 += 1
                merged_array.append(word2[pointer2])
                pointer2 += 1
                char_match_length += 1
            for i in range(char_match_length, len(word1)):
                merged_array.append(word1[pointer1])
                pointer1 += 1
        if len(word1) == len(word2):
            for (char1,char2) in zip(word1,word2):
                merged_array.append(char1)
                merged_array.append(char2)
        
        merged_array = ''.join(merged_array)
        print(merged_array)
        return merged_array

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_count = {} #Will store the count of first string
        second_count = {} #Will store the count of second string

        for char in s:
            if char not in first_count:
                first_count[char] = 1
            else:
                first_count[char] += 1
        
        for char in t:
            if char in second_count:
                second_count[char] += 1
            else:
                second_count[char] = 1
        
        for key in first_count:

            if key not in second_count:
                return False

            if first_count[key] != second_count[key]:
                return False
        
        for key in second_count:

            if key not in first_count:
                return False

            if first_count[key] != second_count[key]:
                return False
        return True
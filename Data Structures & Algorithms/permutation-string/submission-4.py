class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {} #This stores the count of the permutation of s1
        s2_count = {} #This stores the count of the letters in the window of s2

        for char in s1:
            if char in s1_count:
                s1_count[char] += 1
            else:
                s1_count[char] = 1
        
        L = 0
        R = 0

        if len(s1) > len(s2): #Edge case!
            return False 

        while R < len(s2):
            while (R-L) < len(s1):
                if s2[R] in s2_count:
                    s2_count[s2[R]] += 1
                else:
                    s2_count[s2[R]] = 1
                R += 1

            if s1_count == s2_count:
                return True
            
            s2_count[s2[L]] -= 1
            if s2_count[s2[L]] == 0:
                del s2_count[s2[L]]
            
            L += 1
            
        
        return False
        
        

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = {} #Will store the count of our permutation check
        s2_count = {} #Will store the count of our current window 
        for char in s1:
            if char in s1_count:
                s1_count[char] += 1
            else:
                s1_count[char] = 1
        
        L = 0
        R = 0
        if len(s1) > len(s2): #Edge case
            return False

        while R < len(s2):
            while R < len(s2) and (R-L) < len(s1): #For window creates a count for chars changed dict to R -L
                if s2[R] in s2_count:
                    s2_count[s2[R]] += 1
                else:
                    s2_count[s2[R]] = 1
                R += 1

            if s1_count == s2_count: #You can compare dictionaries directly to check counts!
                return True
                
            if s2[L] in s2_count:
                s2_count[s2[L]] -= 1
                if s2_count[s2[L]] == 0:
                    del s2_count[s2[L]]
            L += 1
     
        return False

                
                        


            

            


            


            
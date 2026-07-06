class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_count_s = {} #Hashmap for storing 1st string
        letter_count_t = {}
        #Loop for storying the letters and how often they appear in a has for s
        for letter in s: 
            if letter in letter_count_s:
                letter_count_s[letter] += 1
            else:
                letter_count_s[letter] = 1
        
        #Loop for storing the letters in 2nd string
        for letter in t:
            if letter in letter_count_t:
                letter_count_t[letter] += 1
            else:
                letter_count_t[letter] = 1
            
        #Compare s and t...

        for letter in letter_count_s:
            if letter in letter_count_t:
                if letter_count_s[letter] == letter_count_t[letter]:
                    continue
                else:
                    return False
            else:
                return False
        #Check for letters that are in t but not in s
        for letter in letter_count_t:
            if letter not in letter_count_s:
                return False
                
        return True


    
       
            
            
            
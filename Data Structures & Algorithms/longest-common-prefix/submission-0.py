class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #After asking gpt yh for this bit ---
        if not strs or strs[0] == "": #If the array/list of strings is empty / should also handle if first string is empty
            return ""
        #--
        common_prefix = [] #Array to bench mark answers against first pass
        for char in strs[0]:
            common_prefix.append(char)
        for word in strs:
            
            prefix = []
            for i in range(min(len(common_prefix),len(word))):
                if common_prefix[i] == word[i]:
                    prefix.append(common_prefix[i])

                else:
                    break
            common_prefix = prefix #the new initial value to compare against changes with every iteration
        prefix_string = "".join(common_prefix)
        return prefix_string
                
                    
        


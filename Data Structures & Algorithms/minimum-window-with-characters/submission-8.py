class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {} #Stores the count of t to compare to window
        window = {} #Stores the counts of the sliding window
        
        # New champion variables instead of a list
        min_length = float('inf')
        best_start = -1
        best_end = -1

        #Build out t_count
        for num in t:
            if num in t_count:
                t_count[num] += 1
            else:
                t_count[num] = 1

        def is_valid():
            for char, required_count in t_count.items():
                if window.get(char,0) < required_count:
                    return False
            return True
            
        #Build out sliding window and check
        L = 0
        R = 0

        if len(t) > len(s):
            return ""

        while R < len(s):
            while R < len(s) and not is_valid(): #Keep building out window until t_count items are all within the window
                #Build out sliding window and check
                if s[R] in window:
                    window[s[R]] += 1
                    R += 1
                else:
                    window[s[R]] = 1
                    R += 1

            #Now we shrink the window until we have the shortest window containing the substring
            while is_valid():
                window[s[L]] -= 1
                if window[s[L]] == 0:
                    del window[s[L]]
                L += 1
                
                # Check if this valid window is our new champion
                current_length = (R - 1) - (L - 1) + 1
                if current_length < min_length:
                    min_length = current_length
                    best_start = L - 1
                    best_end = R - 1
                    
        # If min_length changed, we found a valid window. Otherwise, return empty string.
        if min_length != float('inf'):    
            return s[best_start:best_end + 1]
        else:
            return ""
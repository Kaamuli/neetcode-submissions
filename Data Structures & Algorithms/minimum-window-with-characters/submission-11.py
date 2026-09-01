class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {} #Stores the count of t to compare to window
        window = {} #Stores the counts of the sliding window
        shortest_substring = []

        min_length = float('inf')

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
        L=0
        R=0

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
                
                #Store as a valid substring in a tuple, then repeat again starting from new L
                length = R - L
                if length < min_length:
                    shortest_substring = (L-1, R-1)
                    min_length = min(min_length, length)
        if shortest_substring:
            return s[shortest_substring[0]:shortest_substring[1]+1]
        else:
            return ""
            
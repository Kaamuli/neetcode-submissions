class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        R = 0
        count = {}
        res = 0

        for R in range(len(s)):
            if s[R] in count:
                count[s[R]] += 1
            else:
                count[s[R]] = 1
            # If the current window size minus the frequency of the most frequent character > k
            while (R-L+1) - max(count.values()) > k:
                count[s[L]] -= 1
                L += 1 
            
            res = max(res, R-L+1)
    
        return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        R = 0
        max_length = 0

        letters = set()
        
        while R < len(s):
            if s[R] in letters:
                letters.remove(s[L])
                L += 1
            else:
                letters.add(s[R])
                length = (R - L) + 1
                max_length = max(max_length, length)
                R += 1
        return max_length
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()

        while l <= r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            if s[l] != s[r]:
                skipL = s[l + 1: r + 1]
                skipR = s[l:r]
                
                return (skipL == skipL[::-1] or skipR == skipR[::-1])
        return True
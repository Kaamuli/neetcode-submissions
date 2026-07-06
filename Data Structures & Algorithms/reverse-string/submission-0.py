class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        n = len(s)

        while left <= right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1
        return s
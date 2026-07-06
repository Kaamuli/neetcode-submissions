class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [] #initialise array
        n = 2 #Manually input how many times to repeat array.
        for i in range(n):
            for num in nums:
                ans.append(num)
        print(ans)
        return ans
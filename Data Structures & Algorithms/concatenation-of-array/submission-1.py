class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = []
        for i in range(2*n):
            if i < n:
                output.append(nums[i])
            else:
                output.append(nums[i - 2*n])
        print(output)
        return output


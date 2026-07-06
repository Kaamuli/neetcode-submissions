class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_count = {}
        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                return True
        return False
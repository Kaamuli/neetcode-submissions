class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:

            M = L + (R-L)//2

            if nums[M] < nums[M - 1]:
                return nums[M]
            elif nums[R] < nums[L] and nums[M] < nums[R]:
                R = M - 1
            elif nums[R] < nums[L] and nums[M] > nums[R]:
                L = M + 1
            else:
                return nums[L]

            
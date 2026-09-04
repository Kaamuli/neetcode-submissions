class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #Initialise Pointers
        L = 0
        R = len(nums) -1
        M = L + (R-L)//2 #Finds the middle then ceils it if decimal

        while L <= R:
            if nums[M] == target:
                return M
            else:
                if nums[M] < target:
                    L = M + 1
                else:
                    R = M - 1
                M = L + (R-L)//2
        
        return -1
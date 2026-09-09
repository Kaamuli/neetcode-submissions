class Solution:
    def search(self, nums: List[int], target: int) -> int:
         L = 0
         R = len(nums) - 1

         while L <= R:
            M = L + (R-L)//2

            if nums[M] <= nums[M-1]: #less than or equal to to track number
                break #exits while loop
            elif nums[M] > nums[R]:
                L = M + 1
            elif nums[M] < nums[R]:
                R = M - 1
         print(nums[M])
        #Now we have 2 SORTED ARRAYS
         if target == nums[M]:
            return M
         elif M != 0 and target >= nums[0] and target <= nums[M-1]:
            L = 0
            R = M - 1
         else:
            L = M
            R = len(nums) - 1
         
         while L <= R:
            
            M = L + (R-L)//2

            if nums[M] == target:
                return M
            elif nums[M] > target:
                R = M - 1
            else:
                L = M + 1

         return -1
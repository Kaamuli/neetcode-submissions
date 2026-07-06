class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [] #intialise prefix array
        i = 0 #intialise index to move from L -> R
        res = [] #an array for storing the final result
        while i < len(nums):
            if i == 0:
                product = 1 #Intialise array going L->R with product = 1 (outside region)
                prefix.append(product)
            else:
                product *= nums[i - 1]
                prefix.append(product)
            i += 1
        print(prefix)
        suffix = [] #intialise suffix array
        j = len(nums) - 1 #Pointer for suffix array

        while j > -1:
            if j == len(nums) - 1:
                product = 1
                suffix.append(product)
            else:
                product *= nums[j + 1]
                suffix.append(product)
            j -= 1
        print(suffix)
        for pre,suf in zip(prefix, reversed(suffix)):
            res.append(pre * suf)
        print(res)
        return res


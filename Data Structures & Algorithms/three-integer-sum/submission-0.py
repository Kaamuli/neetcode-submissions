class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort() #Sorts it in ascending order

        Triplets = set() #Array to store triples
        for i in range(len(nums)):
            L = 1+i
            R = len(nums) - 1

            while L < R:
                if nums[L] + nums[R] < -nums[i]:
                    L += 1
                elif nums[L] + nums[R] > -nums[i]:
                    R -= 1
                else:
                    Tuple =(nums[L],nums[R],nums[i])
                    Triplets.add(Tuple)
                    L += 1
                    R -= 1

        Answer = [list(Triplet) for Triplet in Triplets]
        print(Answer)
        return Answer

                    
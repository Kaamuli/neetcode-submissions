import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort() #Get it in ascending order

        max_pile = piles[-1] #The largest pile is last.
        k = max_pile
        
        #numbers = [i for i in range(1, max_pile + 1)]

        L = 1
        R = max_pile

        def hourstaken(k):
            hours_taken = 0
            for pile in piles:
                hours_taken += math.ceil(pile/k)
            return hours_taken 

        while L <= R:
            M = L + (R-L)//2
        
            if hourstaken(M) > h:
                L = M + 1
            else:
                R = M - 1
                k = min(k,M)
        
        return k

            

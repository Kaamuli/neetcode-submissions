class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        L=0
        R= len(matrix[0]) - 1
        row = 0

        r_L = 0
        r_R = len(matrix) - 1
        while r_L <= r_R:
            M = r_L + (r_R - r_L)//2

            if (matrix[M][0] <= target) and (matrix[M][-1] >= target): 
                row = M
                break
            elif (matrix[M][0] <= target) and (matrix[M][-1] <= target):
                r_L = M + 1
            else:
                r_R = M - 1

        
        while L <= R:
            M = L + (R-L)//2
            print(M)

            if matrix[row][M] < target:
                L = M + 1
            elif matrix[row][M] > target:
                R = M - 1
            else:
                return True
        
        return False
            
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L_row = 0
        R_row = len(matrix) - 1
        
        while L_row <= R_row:
            M_row = L_row + (R_row - L_row)//2

            if target < matrix[M_row][0]:
                R_row = M_row - 1
            elif target > matrix[M_row][-1]:
                L_row = M_row + 1
            else:
                break #Handle case where correct array is found!         
        
        L = 0
        R = len(matrix[0]) - 1

        while L <= R:
            M = L + (R-L)//2

            if matrix[M_row][M] == target:
                return True
            elif matrix[M_row][M] < target:
                L = M + 1
            else:
                R = M - 1
        
        return False
            
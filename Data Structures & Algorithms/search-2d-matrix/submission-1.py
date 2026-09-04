class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Initialise Row Pointers
        L_row = 0
        R_row = len(matrix) - 1
        n = len(matrix[L_row]) #Counts the number of columns, i.e. array length
        
        while L_row <= R_row:

            M_row = L_row + (R_row - L_row)//2 #Gives u which row is the middle row

            L = 0
            R = len(matrix[M_row]) - 1
            M = L + (R-L)//2

            while L <= R:
                if matrix[M_row][M] == target:
                    return True
                elif matrix[M_row][M] < target:
                    if M == n - 1:
                        L_row = M_row + 1
                        break
                    else:
                        L = M + 1
                        M = L + (R-L) //2
                else:
                    if M == 0:
                        R_row = M_row - 1
                        break
                    else:
                        R = M - 1
                        M = L + (R-L)//2
            
            if L > R:
                return False
        
        return False
    

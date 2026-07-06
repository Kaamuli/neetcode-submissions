class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        counter = set() #Will keep track of numbers seen/not seen
        #check rows
        for i in range(9):
            for j in range(9):
                if board[i][j] not in counter and board[i][j] != ".":
                    counter.add(board[i][j])
                elif board[i][j] == ".":
                    continue
                else:
                    return False
            counter = set()
        
        #check columns
        for j in range(9): #Loop through the columns 1st
            for i in range(9): #Every element in its respective column
                if board[i][j] not in counter and board[i][j] != ".":
                    counter.add(board[i][j])
                elif board[i][j] == ".":
                    continue
                else:
                    return False
            counter = set()
        
        #check subboxes
        starts = [[0,0],[0,3],[0,6],
                 [3,0], [3,3], [3,6],
                 [6,0], [6,3], [6,6]]
        
        for start in starts:
            for i in range(3):
                for j in range(3):
                    if board[start[0]+i][start[1]+j] not in counter and board[start[0]+i][start[1]+j] != ".":
                        counter.add(board[start[0]+i][start[1]+j])
                    elif board[start[0]+i][start[1]+j] == ".":
                        continue
                    else:
                        return False
            counter = set()
        return True
                
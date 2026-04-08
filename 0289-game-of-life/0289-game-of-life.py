class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def check_boundary(i,j):
            return i < len(board) and j<len(board[0]) and i >=0 and j>=0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0
                if check_boundary(i-1,j-1) and (board[i-1][j-1]==-1 or board[i-1][j-1]==1 ):
                    count+=1
                if check_boundary(i-1,j) and (board[i-1][j]==-1 or board[i-1][j]==1 ):
                    count+=1
                if check_boundary(i-1,j+1) and (board[i-1][j+1]==-1 or board[i-1][j+1]==1 ):
                    count+=1
                if check_boundary(i+1,j-1) and (board[i+1][j-1]==-1 or board[i+1][j-1]==1 ):
                    count+=1
                if check_boundary(i+1,j) and (board[i+1][j]==-1 or board[i+1][j]==1 ):
                    count+=1
                if check_boundary(i+1,j+1) and (board[i+1][j+1]==-1 or board[i+1][j+1]==1 ):
                    count+=1
                if check_boundary(i,j-1) and (board[i][j-1]==-1 or board[i][j-1]==1 ):
                    count+=1
               
                if check_boundary(i,j+1) and  (board[i][j+1]==-1 or board[i][j+1]==1 ):
                    count+=1
               
                if count == 3 and board[i][j]==0:
                    board[i][j]=-2
                if count > 3 and board[i][j]==1:
                    board[i][j]=-1
                if count < 2 and board[i][j]==1:
                    board[i][j]=-1

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==-2:
                    board[i][j]=1
                if board[i][j]==-1:
                    board[i][j]=0      



            
        
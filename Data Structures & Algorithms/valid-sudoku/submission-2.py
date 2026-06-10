class Solution:
    def isValidMatrix(self, board: List[List[str]] , i, j)-> bool:
        n = i*3
        m = j*3
        unique = set()
        for i in range(n,n+3):
            for j in range(m,m+3):
                if board[i][j] in unique:
                    print("here1")
                    return False
                elif board[i][j] != ".":
                    unique.add(board[i][j])
        return True



    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board[0])
        i = j = 0
        unique = set()
        while i < n:
            unique.clear()
            while j < n:
                if board[i][j] in unique:
                    return False
                elif board[i][j] != ".":
                    unique.add(board[i][j])
                    j += 1
                else:
                    j += 1
            i += 1
            j = 0

        unique.clear()

        while j < n:
            unique.clear()
            while i < n:
                if board[i][j] in unique:
                    return False
                elif board[i][j] != ".":
                    unique.add(board[i][j])
                    i += 1
                else:
                    i += 1
            j += 1
            i = 0
        unique.clear()

        for i in range(3):
            for j in range(3):
                res = self.isValidMatrix(board, i, j)
                if res == False:
                    return False

        
        return True
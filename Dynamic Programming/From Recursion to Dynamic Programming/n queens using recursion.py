n = 4
board = [ [0 for i in range(n)] for j in range(n)]

def isSafe(board,i,j,n):
    # check for the column
    for row in range(i):
        if board[row][j] == 1:
            return False
    
    x = i
    y = j
    while(x>=0 and y>=0):
        if board[x][y] == 1:
            return False
        x -= 1
        y -= 1
    
    x= i
    y = j
    while(x>=0 and y<=n):
        if board[x][y] == 1:
            return False
        x -= 1
        j += 1
    return True


def solveNQueen(board,n,i):
    if i == n:
        return True

    
    for j in range(n):
        if isSafe(board,i,j,n):
            board[i][j] = 1
            okay = solveNQueen(board,n,i+1)
            if okay:
                return True
            board[i][j] = 0

    return False

solveNQueen(board, n, 0)
print(board)



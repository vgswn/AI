def safe(x,y,board,n):
    for i in range(0,x+1):
        if board[i][y]==1:
            return False
    for i in range(0,y+1):
        if board[x][i]==1:
            return False
    i=x
    j=y
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i=i-1
        j=j-1
    i=x
    j=y
    while i<n and j>=0:
        if board[i][j]==1:
            return False
        i=i+1
        j=j-1
    return True
def btc(board,n,col):
    if col>=n:
        return True
    for i in range(n):
        if safe(i,col,board,n):
            board[i][col]=1
            if btc(board,n,col+1):
                return True
            board[i][col]=0
    return False
n=int(input())
board=[[0 for i in range(n)] for i in range(n)]
if btc(board,n,0):
    print(board)
else:
    print('Not possible')
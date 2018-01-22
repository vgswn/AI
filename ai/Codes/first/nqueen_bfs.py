import queue as q
import copy
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
def bfs(board,n):
    que=q.Queue()
    que.put((board,0))
    vis={}
    vis[(tuple(tuple(x) for x in board))]=1
    while que.empty()==False:
        board,col=que.get()
        #print(board)
        if col==n:
            print(board)
            return
        for i in range(n):
            if safe(i,col,board,n):
                r=copy.deepcopy(board)
                r[i][col]=1
                if vis.__contains__((tuple(tuple(x) for x in r)))==False:
                    vis[(tuple(tuple(x) for x in r))]=1
                    que.put((r,col+1))
    print('Not possible')
n=int(input())
board=[[0 for i in range(n)]for i in range(n)]
bfs(board,n)
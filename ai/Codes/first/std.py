def find_unass(m,n,board):
    for i in range(m):
        for j in range(n):
            print(i,j)
            if board[i][j]==0:
                return [i,j]
    return True
def safe(sn,x,y,stdlist,friendlist,m,n):
    enemylist=[]
    fl=friendlist.get(sn)
    for i in stdlist:
        if fl.__contains__(i)==False and i!=sn:
            enemylist.append(i)
    if x-1>=0 and enemylist.__contains__(board[x-1][y])==True:
        return False
    if y-1>=0 and enemylist.__contains__(board[x][y-1])==True:
        return False
    #print(x+1,m,board)
    if x+1<m and enemylist.__contains__(board[x+1][y])==True:
        return False
    if y+1<n and enemylist.__contains__(board[x][y+1])==True:
        return False
    if x-1>=0 and y-1>=0 and enemylist.__contains__(board[x-1][y-1])==True:
        return False
    if x-1>=0 and y+1<n and enemylist.__contains__(board[x-1][y+1])==True:
        return False
    if x+1<m and y-1>=0 and enemylist.__contains__(board[x+1][y-1])==True:
        return False
    if x+1<m and y+1<n and enemylist.__contains__(board[x+1][y+1])==True:
        return False
    return True

def backtrack(m,n,board,vis,stdlist,friendlist):
    a=find_unass(m,n,board)
    if a==True:
        return a
    x,y=a[0],a[1]
    for sn in stdlist:
        if vis[sn]==0 and safe(sn,x,y,stdlist,friendlist,m,n):
            board[x][y]=sn
            vis[sn]=1
            if backtrack(m,n,board,vis,stdlist,friendlist):
                return True
            vis[sn]=0
            board[x][y]=0
    return False
m,n=input().split(' ')
m,n=int(m),int(n)
stdlist=[]
vis={}
friendlist={}
for i in range(m*n):
    nm=input().split(' ')
    stdlist.append(nm[0])
    ls=[]
    a=int(nm[1])
    id=2
    for j in range(a):
        ls.append(nm[id])
        id=id+1
    friendlist[nm[0]]=ls
    vis[nm[0]]=0
board=[[0 for i in range(n)]for j in range(m)]
print(board)
if backtrack(m,n,board,vis,stdlist,friendlist):
    print(board)
else:
    print('Not solvable')



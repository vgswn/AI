class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
def dfs(arr,n,m,sx,sy,dx,dy,par,d):
    s=Stack()
    vis=[[0 for i in range(m)] for i in range(n)]
    s.push(tuple((sx,sy)))
    vis[sx][sy]=1
    par[sx][sy]=[-1,-1]
    d[sx][sy]=0
    ans=[]
    while s.isEmpty()==False:
        y=s.pop()
        i=y[0]
        j=y[1]
        ans.append(tuple((i,j)))
        if i==dx and j==dy:
            break
        if i-1>=0 and vis[i-1][j]==0 and arr[i-1][j]!='%':
            s.push(tuple((i-1,j)))
            par[i-1][j]=[i,j]
            d[i-1][j]=d[i][j]+1
            vis[i-1][j]=1
        if j-1>=0 and vis[i][j-1]==0 and arr[i][j-1]!='%':
            s.push(tuple((i,j-1)))
            par[i][j-1]=[i,j]
            d[i][j-1]=d[i][j]+1
            vis[i][j-1]=1
        if j+1<m and vis[i][j+1]==0 and arr[i][j+1]!='%':
            s.push(tuple((i,j+1)))
            par[i][j+1]=[i,j]
            d[i][j+1]=d[i][j]+1
            vis[i][j+1]=1
        if i+1<n and vis[i+1][j]==0 and arr[i+1][j]!='%':
            s.push(tuple((i+1,j)))
            par[i+1][j]=[i,j]
            d[i+1][j]=d[i][j]+1
            vis[i+1][j]=1
    print(len(ans))
    for i,j in ans:
        print(i,j)
def pp(x,par,s):
    if x==s:
        print(s[0],s[1])
    elif par[x[0]][x[1]].__eq__([-1,-1]):
        print('No path')
    else:
        pp(par[x[0]][x[1]],par,s)
        print(x[0],x[1])
px,py=input().split(' ')
px,py=(int(px),int(py))
dx,dy=input().split(' ')
dx,dy=(int(dx),int(dy))
n,m=input().split(' ')
n,m=(int(n),int(m))
arr=[]
for i in range(n):
    x=input()
    arr.append(x)
#print(arr)
par=[[[-1,-1] for i in range(m)] for i in range(n)]
d=[[0 for i in range(m)] for i in range(n)]
dfs(arr,n,m,px,py,dx,dy,par,d)
print(d[dx][dy])
pp([dx,dy],par,[px,py])


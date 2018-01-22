import queue
def dfs(arr,n,m,sx,sy,dx,dy,par):
    s=queue.PriorityQueue()
    vis=[[0 for i in range(m)] for i in range(n)]
    d = [[0 for i in range(m)] for i in range(n)]
    s.put(tuple((sx,sy,0)))
    d[sx][sy]=0
    vis[sx][sy]=1
    ans=[]
    par[sx][sy]=[-1,-1]
    #ans=[]
    while s.empty()==False:
        y=s.get()
        #ans.append(tuple(y[0],y[1]))
        i=y[0]
        j=y[1]
        vis[i][j]=1
        ans.append(tuple((i,j)))
        if i==dx and j==dy:
            break
        if i-1>=0 and vis[i-1][j]==0 and arr[i-1][j]!='%':
            d[i-1][j]=d[i][j]+1
            hf=d[i-1][j]+abs(dx-(i-1))+abs(dy-j)
            par[i-1][j]=[i,j]
            s.put(tuple((i-1,j,hf)))
            #vis[i-1][j]=1
        if j-1>=0 and vis[i][j-1]==0 and arr[i][j-1]!='%':
            d[i][j-1]=d[i][j]+1
            par[i ][j-1] = [i, j]
            hf=d[i][j-1]+abs(dx-i)+abs(dy-(j-1))
            s.put(tuple((i,j-1,hf)))
            #vis[i][j-1]=1
        if j+1<m and vis[i][j+1]==0 and arr[i][j+1]!='%':
            d[i][j+1]=d[i][j]+1
            par[i][j+1] = [i, j]
            hf=d[i][j+1]+abs(dx-i)+abs(dy-(j+1))
            s.put(tuple((i,j+1,hf)))
            #vis[i][j+1]=1
        if i+1<n and vis[i+1][j]==0 and arr[i+1][j]!='%':
            d[i+1][j]=d[i][j]+1
            par[i+1][j] = [i, j]
            hf=d[i+1][j]+abs(dx-(i+1))+abs(dy-j)
            s.put(tuple((i+1,j,hf)))
            #vis[i+1][j]=1
    print(d[dx][dy])
def pp(px,py,par,sx,sy,ans):
    ans[0]=ans[0]+1
    if px==sx and py==sy:
        print(px,py)
    elif par[px][py].__eq__([-1,-1]):
        print('No path')
    else:
        x=par[px][py][0]
        y=par[px][py][1]
        pp(x,y,par,sx,sy,ans)
        print(px,py)
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
dfs(arr,n,m,px,py,dx,dy,par)
ans=[0]
pp(dx,dy,par,px,py,ans)
#print(ans[0])


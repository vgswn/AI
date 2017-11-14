import queue as q
def dijk(sx,sy,dx,dy,adj,par,vis,d,n,m):
    pq=q.PriorityQueue()
    pq.put([0,sx,sy])
    d[sx][sy]=0
    while pq.empty()==False:
        a=pq.get()
        x,y=a[1],a[2]
        vis[x][y]=1
        lx=[0,1,1,1,0,-1,-1,-1]
        ly=[1,1,0,-1,-1,-1,0,1]
        dis=[1,1.414,1,1.414,1,1.414,1,1.414]
        for poi in range(8):
            ny=y+ly[poi]
            nx=x+lx[poi]
            if nx>=0 and nx<n and ny>=0 and ny<m and adj[nx][ny]!=-1 and vis[nx][ny]==0 and d[nx][ny]>d[x][y]+dis[poi]:
                par[nx][ny]=[x,y]
                d[nx][ny]=d[x][y]+dis[poi]
                pq.put([d[nx][ny],nx,ny])

def pp(sx,sy,x,y,par):
    if x==sx and y==sy:
        print(x,y,end=' ')
    elif par[x][y]==-1:
        return
    else:
        pp(sx,sy,par[x][y][0],par[x][y][1],par)
        print(x,y,end=' ')

t=int(input())
for h in range(t):
    ai=input().split(' ')
    n,m=int(ai[0]),int(ai[1])
    adj=[[0 for j in range(m)]for i in range(n)]
    dx,dy=0,0
    for i in range(n):
        x=input().split(' ')
        #print(x)
        j=0
        for u in x:
            #print(x[j])
            if u==' 'or u=='':
                continue
            adj[i][j]=int(u)
            if adj[i][j]==1:
                dx,dy=i,j
            j=j+1
    ai=input().split(' ')
    sx,sy=int(ai[0]),int(ai[1])
    par=[[-1 for i in range(m)]for j in range(n)]
    vis=[[0 for i in range(m)]for j in range(n)]
    d=[[10005 for i in range(m)]for j in range(n)]
    dijk(sx,sy,dx,dy,adj,par,vis,d,n,m)
    if d[dx][dy]==10005:
        print(-1)
    else:
        pp(sx,sy,dx,dy,par)
        print()
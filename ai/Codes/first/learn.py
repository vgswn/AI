import queue as q
class my:
    def __init__(self,a,x,y):
        self.first=a
        self.x=x
        self.y=y
    def __lt__(self,other):
        return self.first < other.first
def ucs(sx,sy,dx,dy,par,d,vis,r,c,adj):
    pq=q.PriorityQueue()
    d[sx][sy]=0
    pq.put(my(d[sx][sy]+abs(sx-dx)+abs(sy-dy), sx, sy))
    ans=[]
    while pq.empty()==False:
        a=pq.get()
        x,y=a.x,a.y
        ans.append([x,y])
        vis[x][y]=1
        if x==dx and y==dy:
            break
        if x-1>=0 and vis[x-1][y]==0 and adj[x-1][y]!='%' and d[x-1][y]>d[x][y]+1:
            d[x-1][y]=d[x][y]+1
            par[x-1][y]=[x,y]
            vis[x-1][y]=1
            pq.put(my(d[x-1][y]+abs(x-1-dx)+abs(y-dy),x-1,y))
        if y-1>=0 and vis[x][y-1]==0 and adj[x][y-1]!='%' and d[x][y-1]>d[x][y]+1:
            d[x][y-1]=d[x][y]+1
            par[x][y-1]=[x,y]
            vis[x][y-1]=1
            pq.put(my(d[x][y-1]+abs(x-dx)+abs(y-1-dy),x,y-1))
        if y+1<c and vis[x][y+1]==0 and adj[x][y+1]!='%' and d[x][y+1]>d[x][y]+1:
            d[x][y+1]=d[x][y]+1
            par[x][y+1]=[x,y]
            vis[x][y+1]=1
            pq.put(my(d[x][y+1]+abs(x-dx)+abs(y+1-dy),x,y+1))
        if x+1<r and vis[x+1][y]==0 and adj[x+1][y]!='%' and d[x+1][y]>d[x][y]+1:
            d[x+1][y]=d[x][y]+1
            par[x+1][y]=[x,y]
            vis[x+1][y]=1
            pq.put(my(d[x+1][y]+abs(x+1-dx)+abs(y-dy),x+1,y))



def pp(x, y, sx, sy, par):
    if x == sx and y == sy:
        print(x, y)
    elif par[x][y].__eq__([-1,-1])==True:
        print('No path')
    else:
        pp(par[x][y][0], par[x][y][1], sx, sy, par)
        print(x, y)



sx,sy=input().split(' ')
sx,sy=(int(sx),int(sy))

dx,dy=input().split(' ')
dx,dy=(int(dx),int(dy))

r,c=input().split(' ')
r,c=(int(r),int(c))

adj=[[]for i in range(r)]
for i in range(r):
    x=input()
    for y in x:
        adj[i].append(y)
par=[[]for i in range(r)]
for i in range(r):
    for j in range(c):
        par[i].append([-1,-1])

d=[[100000 for i in range(c)]for i in range(r)]
vis=[[0 for i in range(c)]for i in range(r)]
ucs(sx,sy,dx,dy,par,d,vis,r,c,adj)

print(d[dx][dy])
pp(dx,dy,sx,sy,par)
import random
def clean(adj,x,y,c,n,m,vis):
    flag=0
    for i in range(n+1):
        for j in range(m+1):
            if vis[i][j]==0:
                flag=1
    if flag==0:
        return
    vis[x][y]=1
    if adj[x][y]=='D':
        adj[x][y]='C'
        print('Sucked at ',x,y)
    '''if x-1>=0 and adj[x-1][y]=='D':
        print('going up from ',x,y,' to ',x-1,y)
        clean(adj,x-1,y,c,n,m,vis)
    elif x+1<=n and adj[x+1][y]=='D':
        print('going down from ', x, y, ' to ', x + 1, y)
        clean(adj,x+1,y,c,n,m,vis)
    elif y-1>=0 and adj[x][y-1]=='D':
        print('going left from ', x, y, ' to ', x , y-1)
        clean(adj,x,y-1,c,n,m,vis)
    elif y+1<=m and adj[x][y+1]=='D':
        print('going right from ', x, y, ' to ', x , y+1)
        clean(adj,x,y+1,c,n,m,vis)'''
    if True:
        flag=0
        while flag==0:
            r=random.randrange(4)
            if r==0 and x-1>=0:
                print('going up from ', x, y, ' to ', x - 1, y)
                clean(adj,x-1,y,c,n,m,vis)
                flag=1
            elif r==1 and x+1<=n:
                print('going down from ', x, y, ' to ', x + 1, y)
                clean(adj,x+1,y,c,n,m,vis)
                flag=1
            elif r==2 and y-1>=0:
                print('going left from ', x, y, ' to ', x , y-1)
                clean(adj,x,y-1,c,n,m,vis)
                flag=1
            elif r==3 and y+1<=m:
                print('going right from ', x, y, ' to ', x , y+1)
                clean(adj,x,y+1,c,n,m,vis)
                flag=1

n,m=input().split(' ')
n,m=(int(n),int(m))
adj=[]
vis=[]
for i in range(n):
    adj.append([])
    vis.append([])
    for j in range(m):
        x=random.randrange(2)
        vis[i].append(0)
        if x==0:
            adj[i].append('C')
        else:
            adj[i].append('D')
print(adj)
x=random.randrange(n)
y=random.randrange(m)
c=0
clean(adj,x,y,c,n-1,m-1,vis)
print(vis)
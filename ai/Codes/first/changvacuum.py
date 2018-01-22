import random
def interpret_input(percept):
    if percept[2]=='D':
        state=['Suck']
    else:
        state=['Leave']
    return state
def simple_reflex_agent(percept):
    action=[]
    state=interpret_input(percept)
    x=percept[0]
    y=percept[1]
    n=percept[3]
    m=percept[4]
    if state[0]=='Suck':
        print('Suck at ', x, y)
    r=random.randrange(4)
    if r==0 and x-1>=0:
        print('going up from ', x, y, ' to ', x - 1, y)
        action.append(1)
        action.append(x-1)
        action.append(y)
    elif r==1 and x+1<=n:
        print('going down from ', x, y, ' to ', x + 1, y)
        action.append(1)
        action.append(x+1)
        action.append(y)
    elif r==2 and y-1>=0:
        print('going left from ', x, y, ' to ', x , y-1)
        action.append(1)
        action.append(x)
        action.append(y-1)
    elif r==3 and y+1<=m:
        print('going right from ', x, y, ' to ', x , y+1)
        action.append(1)
        action.append(x)
        action.append(y+1)
    else:
        action.append(0)
    return action
def clean(adj,x,y,c,n,m,vis):
    if c==(n+1)*(m+1):
        return
    action=simple_reflex_agent([x,y,adj[x][y],n,m])
    if vis[x][y]==0:
        c=c+1
    vis[x][y]=1
    if adj[x][y]=='D':
        adj[x][y]='C'
    while action[0]==0:
        action = simple_reflex_agent([x, y, adj[x][y],n,m])
    x=action[1]
    y=action[2]
    clean(adj,x,y,c,n,m,vis)
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

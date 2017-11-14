import copy
import queue as q
def heuristic(arr,k,goal):
    c=0
    f=0
    for i in range(k):
        for j in range(k):
            if arr[i][j]!=f:
                c=c+1
            f=f+1
            #c=c+abs(arr[i][j]-goal[arr[i][j]][0])+abs(arr[i][j]-goal[arr[i][j]][1])
    return c
def goal_test(adj,k):
    f=0
    for i in range(k):
        for j in range(k):
            if adj[i][j]!=f:
                return False
            f=f+1
    return True
def astar(adj,goal,par,k,g):
    d={}
    vis=set()
    d[tuple(tuple(t) for t in adj)]=0
    pq=q.PriorityQueue()
    pq.put(tuple((d[tuple(tuple(t) for t in adj)]+heuristic(adj,k,goal),adj)))
    while pq.empty()==False:
        pr,adj=pq.get()
        vis.add(tuple(tuple(t) for t in adj))
        if goal_test(adj,k)==True:
            break
        x=0
        y=0
        for i in range(k):
            for j in range(k):
                if adj[i][j]==0:
                    x=i
                    y=j
        if x-1>=0:
            ls=copy.deepcopy(adj)
            ls[x-1][y],ls[x][y]=ls[x][y],ls[x-1][y]
            if vis.__contains__(tuple(tuple(t) for t in ls))==False:
                if d.__contains__(tuple(tuple(t) for t in ls))==False:
                    d[tuple(tuple(t) for t in ls)]=d[tuple(tuple(t) for t in adj)]+1
                    pq.put(tuple((heuristic(ls, k, goal), ls)))
                    par[tuple(tuple(t) for t in ls)]=[adj,'UP']
                elif d[tuple(tuple(t) for t in ls)]>d[tuple(tuple(t) for t in adj)]+1:
                    d[tuple(tuple(t) for t in ls)] = d[tuple(tuple(t) for t in adj)] + 1
                    pq.put(tuple((heuristic(ls,k,goal),ls)))
                    par[tuple(tuple(t) for t in ls)]=[adj,'UP']

        if y-1>=0:
            ls=copy.deepcopy(adj)
            ls[x][y-1],ls[x][y]=ls[x][y],ls[x][y-1]
            if vis.__contains__(tuple(tuple(t) for t in ls))==False:
                if d.__contains__(tuple(tuple(t) for t in ls))==False:
                    d[tuple(tuple(t) for t in ls)]=d[tuple(tuple(t) for t in adj)]+1
                    pq.put(tuple((heuristic(ls, k, goal), ls)))
                    par[tuple(tuple(t) for t in ls)]=[adj,'LEFT']
                elif d[tuple(tuple(t) for t in ls)]>d[tuple(tuple(t) for t in adj)]+1:
                    d[tuple(tuple(t) for t in ls)] = d[tuple(tuple(t) for t in adj)] + 1
                    pq.put(tuple(( heuristic(ls, k, goal), ls)))
                    par[tuple(tuple(t) for t in ls)]=[adj,'LEFT']

        if x+1<k:
            ls=copy.deepcopy(adj)
            ls[x+1][y],ls[x][y]=ls[x][y],ls[x+1][y]
            if vis.__contains__(tuple(tuple(t) for t in ls))==False:
                if d.__contains__(tuple(tuple(t) for t in ls))==False:
                    d[tuple(tuple(t) for t in ls)]=d[tuple(tuple(t) for t in adj)]+1
                    pq.put(tuple(( heuristic(ls, k, goal), ls)))
                    par[tuple(tuple(t) for t in ls)]=[adj,'DOWN']
                elif d[tuple(tuple(t) for t in ls)]>d[tuple(tuple(t) for t in adj)]+1:
                    d[tuple(tuple(t) for t in ls)] = d[tuple(tuple(t) for t in adj)] + 1
                    pq.put(tuple((heuristic(ls, k, goal), ls)))
                    par[tuple(tuple(t) for t in ls)]=[adj,'DOWN']

        if y+1<k:
            ls=copy.deepcopy(adj)
            ls[x][y+1],ls[x][y]=ls[x][y],ls[x][y+1]
            if vis.__contains__(tuple(tuple(t) for t in ls))==False:
                if d.__contains__(tuple(tuple(t) for t in ls))==False:
                    d[tuple(tuple(t) for t in ls)]=d[tuple(tuple(t) for t in adj)]+1
                    pq.put(tuple(( heuristic(ls, k, goal), ls)))
                    par[tuple(tuple(t) for t in ls)]=[adj,'RIGHT']
                elif d[tuple(tuple(t) for t in ls)]>d[tuple(tuple(t) for t in adj)]+1:
                    d[tuple(tuple(t) for t in ls)] = d[tuple(tuple(t) for t in adj)] + 1
                    pq.put(tuple(( heuristic(ls, k, goal), ls)))
                    par[tuple(tuple(t) for t in ls)]=[adj,'RIGHT']
    print(d[tuple(tuple(t) for t in g)])


def pp(adj,fm,par):
    if adj.__eq__(fm):
        return
    elif par.__contains__(tuple(tuple(t) for t in adj))==False:
        return
    else:
        pp(par[tuple(tuple(t) for t in adj)][0],fm,par)
        print(par[tuple(tuple(t) for t in adj)][1])


k=int(input())
adj=[[]for i in range(k)]
par={}
goal=[]
for i in range(k):
    for j in range(k):
        x=int(input())
        adj[i].append(x)
        goal.append(tuple((i,j)))

g=[[]for i in range(k)]
f=0
for i in range(k):
    for j in range(k):
        g[i].append(f)
        f=f+1

astar(adj,goal,par,k,g)
pp(g,adj,par)
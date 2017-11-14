import queue as q
import copy
def heu(arr,goal):
    c=0
    for i in range(3):
        for j in range(3):
            if arr[i][j]!=goal[i][j] and arr[i][j]!=0:
                c=c+1
    return c
def astar(adj,goal,par):
    vis={}
    d={}
    d[(tuple(tuple(x) for x in adj))]=0
    pq=q.PriorityQueue()
    pq.put((d[(tuple(tuple(x) for x in adj))]+heu(adj,goal),adj))
    while pq.empty()==False:
        adj=pq.get()[1]
        vis[(tuple(tuple(x) for x in adj))]=1
        if goal.__eq__(adj):
            #print(goal)
            return
        x=0
        y=0
        for i in range(3):
            for j in range(3):
                if adj[i][j]==0:
                    x=i
                    y=j
        if x-1>=0:
            ns=copy.deepcopy(adj)
            ns[x][y],ns[x-1][y]=ns[x-1][y],ns[x][y]
            if vis.__contains__(tuple(tuple(x) for x in ns))==False:
                if d.__contains__(tuple(tuple(x) for x in ns))==False:
                    d[tuple(tuple(x) for x in ns)]=d[tuple(tuple(x) for x in adj)]+1
                    par[tuple(tuple(x) for x in ns)]=adj
                    pq.put((d[(tuple(tuple(x) for x in ns))] + heu(ns, goal), ns))
                elif d[tuple(tuple(x) for x in ns)]>d[tuple(tuple(x) for x in adj)]+1:
                    d[tuple(tuple(x) for x in ns)]=d[tuple(tuple(x) for x in adj)]+1
                    par[tuple(tuple(x) for x in ns)]=adj
                    pq.put((d[(tuple(tuple(x) for x in ns))] + heu(ns, goal), ns))

        if y-1>=0:
            ns=copy.deepcopy(adj)
            ns[x][y],ns[x][y-1]=ns[x][y-1],ns[x][y]
            if vis.__contains__(tuple(tuple(x) for x in ns))==False:
                if d.__contains__(tuple(tuple(x) for x in ns))==False:
                    d[tuple(tuple(x) for x in ns)]=d[tuple(tuple(x) for x in adj)]+1
                    par[tuple(tuple(x) for x in ns)]=adj
                    pq.put((d[(tuple(tuple(x) for x in ns))] + heu(ns, goal), ns))
                elif d[tuple(tuple(x) for x in ns)]>d[tuple(tuple(x) for x in adj)]+1:
                    d[tuple(tuple(x) for x in ns)]=d[tuple(tuple(x) for x in adj)]+1
                    par[tuple(tuple(x) for x in ns)]=adj
                    pq.put((d[(tuple(tuple(x) for x in ns))] + heu(ns, goal), ns))

        if x+1<3:
            ns=copy.deepcopy(adj)
            ns[x][y],ns[x+1][y]=ns[x+1][y],ns[x][y]
            if vis.__contains__(tuple(tuple(x) for x in ns))==False:
                if d.__contains__(tuple(tuple(x) for x in ns))==False:
                    d[tuple(tuple(x) for x in ns)]=d[tuple(tuple(x) for x in adj)]+1
                    par[tuple(tuple(x) for x in ns)]=adj
                    pq.put((d[(tuple(tuple(x) for x in ns))] + heu(ns, goal), ns))
                elif d[tuple(tuple(x) for x in ns)]>d[tuple(tuple(x) for x in adj)]+1:
                    d[tuple(tuple(x) for x in ns)]=d[tuple(tuple(x) for x in adj)]+1
                    par[tuple(tuple(x) for x in ns)]=adj
                    pq.put((d[(tuple(tuple(x) for x in ns))] + heu(ns, goal), ns))

        if y+1<3:
            ns=copy.deepcopy(adj)
            ns[x][y],ns[x][y+1]=ns[x][y+1],ns[x][y]
            if vis.__contains__(tuple(tuple(x) for x in ns))==False:
                if d.__contains__(tuple(tuple(x) for x in ns))==False:
                    d[tuple(tuple(x) for x in ns)]=d[tuple(tuple(x) for x in adj)]+1
                    par[tuple(tuple(x) for x in ns)]=adj
                    pq.put((d[(tuple(tuple(x) for x in ns))] + heu(ns, goal), ns))
                elif d[tuple(tuple(x) for x in ns)]>d[tuple(tuple(x) for x in adj)]+1:
                    d[tuple(tuple(x) for x in ns)]=d[tuple(tuple(x) for x in adj)]+1
                    par[tuple(tuple(x) for x in ns)]=adj
                    pq.put((d[(tuple(tuple(x) for x in ns))] + heu(ns, goal), ns))
def pp(adj,start,par):
    if adj.__eq__(start):
        print(start)
    elif par.__contains__(tuple(tuple(x) for x in adj))==False:
        print('No path')
    else:
        pp(par[tuple(tuple(x) for x in adj)],start,par)
        print(adj)
adj=[[]for i in range(3)]
for i in range(3):
    x=input().split(' ')
    for j in x:
        adj[i].append(int(j))
goal=[[1,2,3],[4,5,6],[7,8,0]]
#print(adj)
par={}
astar(adj,goal,par)
pp(goal,adj,par)
import queue

def dij(adj,par,s,des,n):
    d=[(1000000) for i in range(n)]
    hf=[380,374,253,366,176,193,100,0,80,151,161,77,160,242,241,244,329,199,226,234]
    #par=[(-1)for i in range(n)]
    vis=[0 for i in range(n)]
    d[s]=0
    par[s]=-1
    pq=queue.PriorityQueue()
    pq.put([0,s])
    while pq.empty()==False:
        ls=pq.get()
        x=ls[1]
        vis[x]=1
        for i in range(n):
            if vis[i]==0 and adj[x][i]!=0:
                if d[i]>d[x]+adj[x][i]:
                    par[i]=x
                    d[i]=d[x]+adj[x][i]
                    hv=d[i]+hf[i]
                    pq.put([hv,i])
    print(d[7])
   # print(par)
n=input()
n=int(n)
adj=[]
for i in range(n):
    adj.append([])
    for j in range(n):
        adj[i].append(0)
m=int(input())
for i in range(m):
    u,v,w=input().split(' ')
    u,v,w=(int(u),int(v),int(w))
    adj[u][v]=w
    adj[v][u]=w
print(adj)
par={}
dij(adj,par,6,n-1,n)





'''20
23
0 1 71
1 3 75
3 16 118
16 15 111
15 14 70
14 13 75
13 12 120
0 2 151
3 2 140
2 5 80
5 12 146
5 6 97
12 6 138
2 4 99
6 7 101
4 7 211
7 11 90
7 8 85
8 9 98
9 10 86
8 17 142
17 18 92
18 19 87'''
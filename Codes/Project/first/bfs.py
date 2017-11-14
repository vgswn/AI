
import sys


def prin(adj, s, n):
    d = []
    vis = []
    for i in range(1, n + 1):
        d[i] = -1
        vis[i] = 0
    q = []
    q.append(s)
    d[s]=0
    vis[s]=1
    while len(q)>0:
        t=q.__getitem__(0)
        q.remove(q[0])
        for i in adj[t]:
            if vis[i] == 0:
                vis[i]=1
                q.append(i)
                d[i]=d[t]+6;
    for i in range(1,n+1):
        print(i,end=' ')
    print()

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        n, m = input().strip().split(' ')
        n, m = [int(n), int(m)]
        adj = [[] for i in range(n + 1)]
        for a1 in range(m):
            u, v = input().strip().split(' ')
            u, v = [int(u), int(v)]
            adj[u].append(v)
            adj[v].append(u)
        s = int(input().strip())
        prin(adj, s, n)

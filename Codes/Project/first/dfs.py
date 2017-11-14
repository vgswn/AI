vis=[]
adj=[]
def dfs(x):
    stac=[]
    vis[x]=1
    stac.append(x)
    while len(stac)>0:
        t=stac.pop()
        #print(t)
        for u in adj[t]:
            if vis[u]==0:
                vis[u]=1
                stac.append(u)


n, m = input().split(' ')
n, m = (int(n), int(m))
for i in range(n + 1):
    adj.append([])

for i in range(m):
    a, b = input().split(' ')
    a, b = (int(a), int(b))
    adj[a].append(b)
    adj[b].append(a)
for i in range(n + 1):
    vis.append(0)
x = int(input())
dfs(x)
ans = 0
for i in range(1, n + 1):
    if vis[i] == 0:
        ans = ans + 1
print(ans)

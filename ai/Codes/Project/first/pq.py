"""import heapq
class my:
    def __init__(self,a,b):
        self.first=a
        self.second=b
    def __lt__(self,other):
        return self.second > other.second
pq=[]
heapq.heappush(pq,my(2,5))
heapq.heappush(pq,my(3,4))
d=my(3,6)
heapq.heappush(pq,d)
f={}
f[1]=2
if f.__contains__(1):
    del f[1]
print(pq,len(pq))
pq.remove(d)
print(len(pq))
print(heapq.heappop(pq).first)
print(heapq.heappop(pq).first)
print(len(pq))
a=tuple((1,2))
print(a[0])"""

'''import queue as q
class my:
    def __init__(self,a,b):
        self.first=a
        self.second=b
    def __lt__(self,other):
        return self.second < other.second
def dij(s,vis,n,d,adj):
    hm={}
    pq=q.PriorityQueue()
    d[s]=0
    f=my(s,0)
    pq.put(f)
    while not pq.empty():
        t=pq.get()
        u=t.first
        vis[u]=1
        for i in adj[u]:
            if vis[i[0]]==0 and d[i[0]] > d[u]+i[1]:
                d[i[0]]=d[u]+i[1]
                f=my(i[0],d[i[0]])
                pq.put(f)
t = 1
for a0 in range(t):
    n,m=input().split(' ')
    n,m=(int(n),int(m))
    adj=[[]]
    d=[]
    for i in range(n+1):
        adj.append([])
        d.append(pow(10,20))
    dt={}
    while m>0:
        m=m-1
        a,b,w=input().split(' ')
        a,b,w=(int(a),int(b),int(w))
        if a>b:
            a,b=b,a
        if dt.__contains__(tuple((a,b))) and dt[tuple((a,b))]>w and a!=b:
            dt[tuple((a,b))]=w
        elif dt.__contains__(tuple((a,b)))==False and a!=b:
            dt[tuple((a,b))]=w
    for k,v in dt.items():
        adj[k[0]].append(tuple((k[1],v)))
        adj[k[1]].append(tuple((k[0],v)))
    s=1
    vis=[]
    for i in range(n+1):
        vis.append(0)
    dij(s,vis,n,d,adj)
    for i in range(1,n+1):
        if i!=s:
            if d[i]==pow(10,20):
                d[i]=-1
            print(d[i],end=' ')
    print()'''

import queue as q
class my:
    def __init__(self,a,b):
        self.first=a
        self.second=b
    def __lt__(self,other):
        if self.first!=other.first:
            return self.first > other.first
        else:
            return self.second < other.second


pq=q.PriorityQueue()
pq.put(my(5,6))
pq.put(my(10,4))
pq.put(my(5,3))
print(pq.get().first)
print(pq.get().second)



pq=q.PriorityQueue()
pq.put((8,[3,4]))
pq.put((9,[1,2]))
print(pq.get()[1])
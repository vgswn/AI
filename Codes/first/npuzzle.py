import queue
import copy
def hf(arr,n):
    h1,h2=0,0
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=n*i+j:
                h1=h1+1
            v=arr[i][j]
            x=v//n
            y=v%n
            h2=h2+abs(x-i)+abs(y-j)
    if h1>h2:
        return h1
    else:
        return h2
def bfs(arr,par,goal,n):
    vis=[]
    d={}
    q=queue.PriorityQueue()
    q.put(tuple((arr,0)))
    d[tuple(tuple(x) for x in arr)]=0
    vis.append(arr)
    while not q.empty():
        ls,gn=q.get()
        x=0
        y=0
        if ls.__eq__(goal):
            break
        vis.append(ls)
        #print(ls)
        for i in range(n):
            for j in range(n):
                if ls[i][j]==0:
                    x=i
                    y=j
        #print(x,y)
        cs = copy.deepcopy(ls)
        if x-1>=0:
            cs[x-1][y],cs[x][y]=cs[x][y],cs[x-1][y]
            if vis.__contains__(cs)==False:
                par[tuple(tuple(x) for x in cs)]=ls
                ds=hf(cs,n)
                d[tuple(tuple(x) for x in cs)] = d[tuple(tuple(x) for x in ls)]+1
                ds=ds+d[tuple(tuple(x) for x in cs)]
                q.put(tuple((cs,ds)))
        cs=copy.deepcopy(ls)
        if x+1<n:
            cs[x+1][y],cs[x][y]=cs[x][y],cs[x+1][y]
            if vis.__contains__(cs)==False:
                ds=hf(cs,n)
                #print(tuple(tuple(x) for x in cs))
                d[tuple(tuple(x) for x in cs)] = d[tuple(tuple(x) for x in ls)]+1
                ds=ds+d[tuple(tuple(x) for x in cs)]
                q.put(tuple((cs,ds)))
                par[tuple(tuple(x) for x in cs)]=ls
        cs = copy.deepcopy(ls)
        if y+1<3:
            cs[x][y+1],cs[x][y]=cs[x][y],cs[x][y+1]
            if vis.__contains__(cs)==False:
                ds=hf(cs,n)
                d[tuple(tuple(x) for x in cs)] = d[tuple(tuple(x) for x in ls)]+1
                ds=ds+d[tuple(tuple(x) for x in cs)]
                q.put(tuple((cs,ds)))
                par[tuple(tuple(x) for x in cs)]=ls
        cs = copy.deepcopy(ls)
        if y-1>=0:
            cs[x][y-1],cs[x][y]=cs[x][y],cs[x][y-1]
            if vis.__contains__(cs)==False:
                ds=hf(cs,n)
                d[tuple(tuple(x) for x in cs)] = d[tuple(tuple(x) for x in ls)]+1
                ds=ds+d[tuple(tuple(x) for x in cs)]
                q.put(tuple((cs,ds)))
                par[tuple(tuple(x) for x in cs)]=ls
    #print(vis)
def pp(arr,par,start,x,ans,n):
    if start.__eq__(arr):
        #print(arr)
        return
    elif tuple(tuple(x) for x in arr) not in par:
        print('Not exist')
    else:
        pp(par[tuple(tuple(x) for x in arr)],par,start,x,ans,n)
        x[0] = x[0] + 1
        a,b,c,d=0,0,0,0
        for i in range(n):
            for j in range(n):
                if arr[i][j]==0:
                    a=i
                    b=j
        df=par[tuple(tuple(x) for x in arr)]
        for i in range(n):
            for j in range(n):
                if df[i][j] == 0:
                    c = i
                    d = j
        if d-1==b:
            ans.append('LEFT')
        elif d+1==b:
            ans.append('RIGHT')
        elif c-1==a:
            ans.append('UP')
        else:
            ans.append('DOWN')
        #print(arr)
n=input()
n=int(n)
arr=[[] for i in range(n)]
ca=[]
j=0
k=0
ca=[]
for i in range(n*n):
    x=input()
    x=int(x)
    arr[j].append(x)
    ca.append(x)
    k=k+1
    if k>=n:
        j=j+1
        k=0
goal=[[] for i in range(n)]
j=0
for i in range(n):
    for j in range(n):
        goal[i].append(j)
        j=j+1
par={}
inv=0
#print(ca)
for i in range(n*n):
    for j in range(i+1,n*n):
        if ca[i]!=0 and ca[j]!=0 and ca[i]>ca[j]:
            inv=inv+1
            #print(ca[i],ca[j])
#print(inv)
if inv%2==1:
    print('No path')
else:
    x=[0]
    bfs(arr,par,goal,n)
    ans=[]
    pp(goal,par,arr,x,ans,n)
    print(x[0])
    for i in ans:
        print(i)

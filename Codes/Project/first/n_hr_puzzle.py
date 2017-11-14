import queue as q
import copy
dt={}
par={}
def hf(ls,k):
    ans=0
    x=0
    for i in range(k):
        for j in range(k):
            if ls[i][j]!=x and x!=0:
                ans=ans+1
            #ans=ans+abs(i-dt[ls[i][j]][0])+abs(j-dt[ls[i][j]][1])
    return ans
def astar(start,k,goal):
    vis=set()
    pq=q.PriorityQueue()
    d={}
    d[tuple(tuple(x) for x in start)]=0
    #print(d[tuple(tuple(x) for x in start)])
    pq.put([start,0])
    while pq.empty()==False:
        ls,x=pq.get()
        vis.add(tuple(tuple(x) for x in ls))
        for i in range(k):
            for j in range(k):
                if ls[i][j]==0:
                    x=i
                    y=j
        #print(x,y)
        if tuple(tuple(x) for x in ls).__eq__(tuple(tuple(x) for x in goal)):
            break
        cs = copy.deepcopy(ls)
        if x-1>=0:
            cs[x-1][y],cs[x][y]=cs[x][y],cs[x-1][y]
            if vis.__contains__(tuple(tuple(x) for x in cs))==False and (d.__contains__(tuple(tuple(x) for x in cs))==False or d[tuple(tuple(x) for x in cs)]>d[tuple(tuple(x) for x in ls)]+1):
                par[tuple(tuple(x) for x in cs)]=[ls,"UP"]
                d[tuple(tuple(x) for x in cs)]=d[tuple(tuple(x) for x in ls)]+1
                hv=d[tuple(tuple(x) for x in cs)]+hf(cs,k)
                pq.put([cs,hv])
        cs=copy.deepcopy(ls)
        if x+1<k:
            cs[x+1][y],cs[x][y]=cs[x][y],cs[x+1][y]
            if vis.__contains__(tuple(tuple(x) for x in cs)) == False and (d.__contains__(tuple(tuple(x) for x in cs)) == False or d[tuple(tuple(x) for x in cs)] > d[tuple(tuple(x) for x in ls)] + 1):
                par[tuple(tuple(x) for x in cs)] = [ls, "DOWN"]
                d[tuple(tuple(x) for x in cs)]=d[tuple(tuple(x) for x in ls)]+1
                hv=d[tuple(tuple(x) for x in cs)]+hf(cs,k)
                pq.put([cs,hv])
        cs = copy.deepcopy(ls)
        if y+1<k:
            cs[x][y+1],cs[x][y]=cs[x][y],cs[x][y+1]
            if vis.__contains__(tuple(tuple(x) for x in cs)) == False and (d.__contains__(tuple(tuple(x) for x in cs)) == False or d[tuple(tuple(x) for x in cs)] > d[tuple(tuple(x) for x in ls)] + 1):
                par[tuple(tuple(x) for x in cs)] = [ls, "RIGHT"]
                d[tuple(tuple(x) for x in cs)]=d[tuple(tuple(x) for x in ls)]+1
                hv=d[tuple(tuple(x) for x in cs)]+hf(cs,k)
                pq.put([cs,hv])
        cs = copy.deepcopy(ls)
        if y-1>=0:
            cs[x][y-1],cs[x][y]=cs[x][y],cs[x][y-1]
            if vis.__contains__(tuple(tuple(x) for x in cs)) == False and (d.__contains__(tuple(tuple(x) for x in cs)) == False or d[tuple(tuple(x) for x in cs)] > d[tuple(tuple(x) for x in ls)] + 1):
                par[tuple(tuple(x) for x in cs)] = [ls, "LEFT"]
                d[tuple(tuple(x) for x in cs)]=d[tuple(tuple(x) for x in ls)]+1
                hv=d[tuple(tuple(x) for x in cs)]+hf(cs,k)
                pq.put([cs,hv])
    print(d[tuple(tuple(x) for x in goal)])
def pp(arr,start):
    if start.__eq__(arr):
        return
    elif tuple(tuple(x) for x in arr) not in par:
        print('Not exist')
    else:
        pp(par[tuple(tuple(x) for x in arr)][0],start)
        print(par[tuple(tuple(x) for x in arr)][1])
k=int(input())
goal=[]
x=0
for i in range(k):
    goal.append([])
    for j in range(k):
        goal[i].append(x)
        x=x+1
#print(goal)
x=0
y=0
for i in range(k*k):
   dt[i]=[x,y]
   y=(y+1)%k
   if (i+1)%k==0:
       x=x+1
#print(dt)
s=[]
for i in range(k*k):
    x=int(input())
    s.append(x)
st=[]
x=0
for i in range(k):
    st.append([])
    for j in range(k):
        st[i].append(s[x])
        x=x+1
#print(hf(st,k))
#print(st)
astar(st,k,goal)
pp(goal,st)
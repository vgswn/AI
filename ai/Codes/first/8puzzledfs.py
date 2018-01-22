import copy
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)
def dfs(arr,par,goal,vis,ls,flag):
    if flag.__eq__([1]):
        return
    vis.add(tuple(tuple(x) for x in arr))
    print(arr)
    if True:
        vis.add(tuple(tuple(x) for x in arr))
        par[tuple(tuple(x) for x in arr)] = ls
        x=0
        y=0
        if arr.__eq__(goal):
            flag[0]=1
            return
        for i in range(3):
            for j in range(3):
                if arr[i][j]==0:
                    x=i
                    y=j
        cs = copy.deepcopy(arr)
        if x-1>=0:
            cs[x-1][y],cs[x][y]=cs[x][y],cs[x-1][y]
            if vis.__contains__(tuple(tuple(x) for x in cs))==False:
                dfs(cs,par,goal,vis,arr,flag)
        cs=copy.deepcopy(arr)
        if x+1<3:
            cs[x+1][y],cs[x][y]=cs[x][y],cs[x+1][y]
            if vis.__contains__(tuple(tuple(x) for x in cs))==False:
                dfs(cs, par, goal, vis, arr,flag)
        cs = copy.deepcopy(arr)
        if y+1<3:
            cs[x][y+1],cs[x][y]=cs[x][y],cs[x][y+1]
            if vis.__contains__(tuple(tuple(x) for x in cs))==False:
                dfs(cs, par, goal, vis, arr,flag)
        cs = copy.deepcopy(arr)
        if y-1>=0:
            cs[x][y-1],cs[x][y]=cs[x][y],cs[x][y-1]
            if vis.__contains__(tuple(tuple(x) for x in cs))==False:
                dfs(cs, par, goal, vis, arr,flag)
def pp(arr,par,start):
    if start.__eq__(arr):
        print(arr)
    elif tuple(tuple(x) for x in arr) not in par:
        print('Not exist')
    else:
        pp(par[tuple(tuple(x) for x in arr)],par,start)
        print(arr)
arr=[[] for i in range(3)]
ca=[]
for i in range(3):
    x=input().split(' ')
    arr[i].append(int(x[0]))
    arr[i].append(int(x[1]))
    arr[i].append(int(x[2]))
    ca.append(int(x[0]))
    ca.append(int(x[1]))
    ca.append(int(x[2]))
goal=[[1,2,3],[4,5,6],[7,8,0]]
par={}
inv=0
print(ca)
for i in range(9):
    for j in range(i+1,9):
        if ca[i]!=0 and ca[j]!=0 and ca[i]>ca[j]:
            inv=inv+1
            #print(ca[i],ca[j])
#print(inv)
if inv%2==1:
    print('No path')
else:
    dfs(arr,par,goal,set(),[],[0])
    #pp(goal,par,arr)

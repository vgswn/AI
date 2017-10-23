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
def dfs(arr,par,goal,limit,flag):
    vis=set()
    s=Stack()
    s.push(arr)
    vis.add(tuple(tuple(x) for x in arr))
    new={}
    new[tuple(tuple(x) for x in arr)]=0

    while not s.isEmpty():

        ls=s.pop()
        limit_now = 1 + new[tuple(tuple(x) for x in ls)]
        if limit_now>limit:
            print(limit_now,limit_now,'no')
            #print('no')
            break
        x=0
        y=0
        print(ls)
        if ls.__eq__(goal):
            print('yes')
            flag[0]=1
            #print(ls)
            break
        #print(ls)
        for i in range(3):
            for j in range(3):
                if ls[i][j]==0:
                    x=i
                    y=j
        #print(x,y)
        cs = copy.deepcopy(ls)
        if x-1>=0:
            cs[x-1][y],cs[x][y]=cs[x][y],cs[x-1][y]
            if vis.__contains__(tuple(tuple(x) for x in cs))==False:
                par[tuple(tuple(x) for x in cs)]=ls
                s.push(cs)
                new[tuple(tuple(x) for x in cs)]=limit_now
                vis.add(tuple(tuple(x) for x in ls))
        cs=copy.deepcopy(ls)
        if x+1<3:
            cs[x+1][y],cs[x][y]=cs[x][y],cs[x+1][y]
            if vis.__contains__(tuple(tuple(x) for x in cs))==False:
                s.push(cs)
                new[tuple(tuple(x) for x in cs)] = limit_now
                par[tuple(tuple(x) for x in cs)]=ls
                vis.add(tuple(tuple(x) for x in ls))
        cs = copy.deepcopy(ls)
        if y+1<3:
            cs[x][y+1],cs[x][y]=cs[x][y],cs[x][y+1]
            if vis.__contains__(tuple(tuple(x) for x in cs))==False:
                s.push(cs)
                new[tuple(tuple(x) for x in cs)] = limit_now
                vis.add(tuple(tuple(x) for x in ls))
                par[tuple(tuple(x) for x in cs)]=ls
        cs = copy.deepcopy(ls)
        if y-1>=0:
            cs[x][y-1],cs[x][y]=cs[x][y],cs[x][y-1]
            if vis.__contains__(tuple(tuple(x) for x in cs))==False:
                s.push(cs)
                new[tuple(tuple(x) for x in cs)] = limit_now
                vis.add(tuple(tuple(x) for x in ls))
                par[tuple(tuple(x) for x in cs)]=ls
    #print(vis)
def pp(arr,par,start):
    '''if start.__eq__(arr):
        print(arr)
    elif tuple(tuple(x) for x in arr) not in par:
        print('Not exist')
    else:
        pp(par[tuple(tuple(x) for x in arr)],par,start)
        print(arr)'''
    while start.__eq__(arr)==False:
        print(arr)
        arr=par[tuple(tuple(x) for x in arr)]
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
goal=[[3,1,2],[6,4,5],[7,8,0]]
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
    flag={}
    flag[0]=0
    for i in range(10000):
        dfs(arr,par,goal,i,flag)
        if flag[0]==1:

            pp(goal,par,arr)
            break
        par={}


'''import heapq

class Myheap(object):
    def __init__(self,val):
        self.val=val

    def __lt__(self, other): return self.val < other.val

    def __eq__(self, other): return self.val == other.val

    def __gt__(self, other): return self.val > other.val

pq=[]
heapq.heappush(pq,Myheap(5))
heapq.heappush(pq,Myheap(6))
print(heapq.heappop(pq).val)'''





"""import functools
class Boy:
    def __init__(self,x,y):
        self.name=x
        self.addr=y
    def prin(self):
        print(self.name,self.addr)
class Miser(Boy):
    def __init__(self,x,y,z):
        super().__init__(x,y)
        self.type=z
    def print(self):
        print(self.type)
ob=Miser("Rohan","LA","Miser")
ob.print()
po=Boy("Tanmay","LA")
po.prin()
print(1)
a=input()
a=int(a)
print(a)
arr=[]
for i in range(1,a):
    arr.append(a-i)
    print(i,end=' ')
print()
for i in range(0,arr.__len__()):
    print(arr[i],end=' ')
def cmpp(a,b):
    if a>b:
        return 1;
    elif a<b:
        return -1;
    return 0;
sorted(arr,key=functools.cmp_to_key(cmpp))
print(arr)
ap=[(1,2)]
ap.append((2,3))
print(ap)
print(ap[0])
for a,b in ap:
    print(a,b)"""

import queue
def bfs(n,par):
    q=queue.Queue()
    vis=[]
    q.put((n,n,'L'))
    par[(n,n,'L')]=(-1,-1,'N')
    while not q.empty():
        ls=q.get()
        m=ls[0]
        c=ls[1]
        vis.append(ls)
       # print(vis)
        if m==0 and n==0 and ls[2]=='R':
            break
        if ls[2]=='L':
            if m-1>=0:
                lsm=m-1
                rsm=n-(m-1)
                lsc=c
                rsc=n-c
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                   # print(nl)
                    q.put(nl)
                    vis.append(nl)
                    par[nl]=ls
            if c-1>=0:
                lsm=m
                rsm=n-m
                lsc=c-1
                rsc=n-(c-1)
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.put(nl)
                   # print(nl)
                    vis.append(nl)
                    par[nl]=ls
            if m-1>=0 and c-1>=0:
                lsm=m-1
                rsm=n-(m-1)
                lsc=c-1
                rsc=n-(c-1)
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.put(nl)
                   # print(nl)
                    vis.append(nl)
                    par[nl]=ls
            if m-2>=0:
                lsm=m-2
                rsm=n-(m-2)
                lsc=c
                rsc=n-c
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.put(nl)
                  #  print(nl)
                    vis.append(nl)
                    par[nl]=ls
            if c-2>=0:
                lsm=m
                rsm=n-m
                lsc=c-2
                rsc=n-(c-2)
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.put(nl)
                   # print(nl)
                    vis.append(nl)
                    par[nl]=ls
        else:
            rm=n-m
            rc=n-c
            if rm-1>=0:
                lsm=m+1
                rsm=rm-1
                lsc=c
                rsc=rc
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.put(nl)
                    vis.append(nl)
                    par[nl]=ls
            if rc-1>=0:
                lsm=m
                rsm=rm
                lsc=c+1
                rsc=rc-1
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.put(nl)
                    vis.append(nl)
                    par[nl]=ls
            if rm-1>=0 and rc-1>=0:
                lsm=m+1
                rsm=rm-1
                lsc=c+1
                rsc=rc-1
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.put(nl)
                    vis.append(nl)
                    par[nl]=ls
            if rm-2>=0:
                lsm=m+2
                rsm=rm-2
                lsc=c
                rsc=rc
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.put(nl)
                    vis.append(nl)
                    par[nl]=ls
            if rc-2>=0:
                lsm=m
                rsm=rm
                lsc=c+2
                rsc=rc-2
                if ls[2]=='L':
                    nl=(lsm,lsc,'R')
                else:
                    nl=(lsm,lsc,'L')
                if (lsm==0 or lsm>=lsc) and (rsm==0 or rsm>=rsc) and vis.__contains__(nl)==False:
                    q.put(nl)
                    vis.append(nl)
                    par[nl]=ls

def pp(ls,s,par):
    if ls.__eq__(s):
        print(s)
    elif ls not in par:
        print('Not exist')
        return
    else:
        pp(par[ls],s,par)
        print(ls)
n=input()
n=int(n)
par={}
bfs(n,par)
#print(par)
pp((0,0,'R'),(n,n,'L'),par)
q=queue.Queue()
q.put(1)
print(q.get())




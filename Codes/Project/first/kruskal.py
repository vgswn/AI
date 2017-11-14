import functools
par=[]
adj=[]
def cmpp(a,b):
    if a[2]<b[2]:
        return -1
    elif a[2]>b[2]:
        return 1
    else:
        return 0
def fp(x):
    if x==par[x]:
        return x
    else:
        par[x]=fp(par[x])
        return par[x]
def uni(a,b,w,ans):
    pa,pb=fp(a),fp(b)
    if pa!=pb:
        par[pa]=pb
        ans=ans+w
    return ans
ans=0
ls=input().split(' ')
n,m=(int(ls[0]),int(ls[1]))
for i in range(n+1):
    par.append(i)
for i in range(m):
    a,b,w=input().split(' ')
    a,b,w=(int(a),int(b),int(w))
    adj.append(tuple((a,b,w)))
adj=sorted(adj,key=functools.cmp_to_key(cmpp))
for a,b,w in adj:
    ans=uni(a,b,w,ans)
print(ans)
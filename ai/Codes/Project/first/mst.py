import functools
def cmp(a,b):
    if a[2]<b[2]:
        return -1
    elif a[2]>b[2]:
        return 1
    else:
        return 0
par=[]
def fp(x):
    if x==par[x]:
        return x
    else:
        d=fp(par[x])
        par[x]=d
        return par[x]
def uni(a,b,w,ans):
    pa,pb=fp(a),fp(b)
    if pa!=pb:
        par[pa]=pb
        ans=ans+w
    return ans
adj=[]
ans=0
n,m=input().split(' ')
n,m=(int(n),int(m))
for i in range(n+1):
    par.append(i)
for i in range(m):
    a,b,w=input().split(' ')
    a,b,w=(int(a),int(b),int(w))
    adj.append(tuple((a,b,w)))
adj=sorted(adj,key=functools.cmp_to_key(cmp))
for a,b,w in adj:
    ans=uni(a,b,w,ans)
print(ans)
import math
n=input()
n=n.split()
a,b,c,d=n
a=int(a)
b=int(b)
c=int(c)
d=int(d)
#print(a,b,c,d)
i=2
etf=c
def mexp(a,b,m):
    if b == 0:
        return 1
    tmp=mexp(a,b//2,m)
    if b%2 == 0:
        return (tmp*tmp)%m
    else:
        return (((tmp*tmp)%m)*(a%m))%m
k=c
while i*i <= c:
    if c%i == 0:
        etf=etf*(i-1)
        etf=etf//i
        while c%i == 0:
            c=c//i
    i=i+1
if c>1:
    etf=etf*(c-1)
    etf=etf//c
print(etf)
c=k
ans=1
ans=mexp(a,b,d)*mexp(c,etf-1,d)
ans=ans%d
print(ans)
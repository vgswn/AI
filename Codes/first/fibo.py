def fib(n):
    a=1
    b=1
    while a<n:
         print(a,end=' ')
         a,b=b,a+b

d={}
d['2']=2
d['3']=d['2']+1
print(d['3'])
d['3']=d['2']+4
print(d['3'])
d[((1,2),(3,4))]=1
d[((1,2),(3,44))]=d[((1,2),(3,4))]+1
print(d[((1,2),(3,44))])
cs=[[1,2],[3,4]]
d[(tuple(tuple(x) for x in cs))]=4
print(d[(tuple(tuple(x) for x in cs))])

""" arr=[0]*100001
s=[0]*100001
def sieve():
    arr[1]=1;
    for i in range(2,100001):
        if arr[i] == 0:
            for j in range(2*i,100001,i):
                arr[j]=1
    for i in range(2,100001):
        if arr[i] == 0:
            s[i]=s[i-1]+1
        else:
            s[i]=s[i-1]
sieve()
t=input()
t=int(t)
while t>0:
    l=input()
    l=l.split(sep=' ')
   # print(l)
    a=int(l[0])
    b=int(l[1])
    print(s[b]-s[a-1])
    t=t-1
x=list(input().split())
print(x)
print(int(x[0]))"""

t=int(input())
while t>0:
    x=input().split()
    a=x[0]
    b=x[1]
    try:
        a=int(a)
        b=int(b)
        print(a//b)
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    t=t-1

t=int(input())
dict={}
lis=[]
while t>0:
    x=input()
    lis.append(x)
    if x not in dict:
        dict[x]=1
    else:
        dict[x]=dict[x]+1
    t=t-1
print(len(dict))
for i in lis:
    if i in dict:
        print(dict[i],end=' ')
        dict.pop(i)
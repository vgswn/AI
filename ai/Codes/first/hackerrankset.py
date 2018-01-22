n,m = input().split(' ')
n=int(n)
m=int(m)
arr = []
x = list(map(int,input().split()))
for i in x:
    arr.append(i)
a = set()
b = set()
x = list(map(int,input().split()))
for i in x:
    a.add(i)
x = list(map(int,input().split()))
for i in x:
    b.add(i)
ans=0
#print(a,b)
for i in range(n):
    if arr[i] in a:
        ans=ans+1
    elif arr[i] in b:
        ans=ans-1
print(ans)
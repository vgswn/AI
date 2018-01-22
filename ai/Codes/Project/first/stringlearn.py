n = int(input().strip())
s = input().strip()
k = int(input().strip())
ans=''
for i in s:
    d=ord(i)
    if d>=65 and d<=90:
        d=d+k
        if d>90:
            d=65+(d-90-1)
        ans=ans+chr(d)
    elif d>=97 and d<=122:
        d=d+k
        if d>122:
            d=97+(d-122-1)
        ans=ans+chr(d)
    else:
        ans=ans+i
print(ans)

s=input()
cnt={}
for i in range(97,122):
    cnt[i]=0
for i in s:
    i=i.lower()
    d=ord(i)
    if d>=97 and d<=122:
        cnt[d]=cnt[d]+1
ans=0
for i in range(97,122):
    if cnt[i]==0:
        ans=1
if ans==0:
    print('YES')
else:
    print('NO')

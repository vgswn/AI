n=int(input())
arr=[]
for i in range(n):
    a=(input())
    arr.append(a)
if 'hey' in arr:
    print("yippy")
else:
    pass
b="hey"
#b[0]='k'
i = 5
j=10
j=0
def f(arg=i,bb=j):
    print(arg,bb)
    bb=3

i = 6
f()
f()
pil=(1,2,3)
pil=pil.__add__((4,))
pile=[1,2,3]
print(pil,type(pil),pile,type(pile))
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[0],reverse=True)
print(pairs)

print(pairs.__getitem__(1))

bas=['cb','ab','cb']
for i in sorted(set(bas)):
    print(i)

print(__name__);
class Palindrome:

    @staticmethod
    def is_palindrome(word):
        word=word.lower()
        for i in range(0,word.__len__()//2):
            if word[i] != word[word.__len__()-1-i]:
                return False
        return True

print(Palindrome.is_palindrome('Deleveled'))
def capitalize(string):
    ans=""
    r=""
    for i in range(0,len(string)):
        if string[i] != ' ':
            if r == "":
               r=r+string[i]
               r=r.upper()
               #print(r)
            else:
                r=r+string[i]
        else:
            ans=ans+r
            ans=ans+" "
            r=""
    return ans+r
print(capitalize("hello world"))
print(chr(65))
n=input()
n=int(n)
k=n-1
ch=97+n-1
l=1
lst=[]
for i in range(1,n+1):
    x=0
    y=""
    for j in range(1,2*k+1):
        x=x+1
        y=y+"-"
        print('-',end='')
    for p in range(0,l):
        x=x+2
        print(chr(ch),end='')
        y=y+chr(ch)
        if n != 1:
            print('-',end='')
            y=y+"-"
        ch = ch - 1
    if i == 1:
        for j in range(1,2*k):
            x=x+1
            y=y+"-"
            print('-',end='')
    else:
        ch=ch+1
        for p in range(0,l-1):
            ch=ch+1
            y=y+chr(ch)
            print(chr(ch), end='')
            if p == l-2:
                x=x+1
                continue
            x = x + 2
            print('-', end='')
            y=y+"-"
    k = k - 1
    l=l+1
    ch=97+n-1
    if i == n:
        continue
    #for j in range(x,4*n-3):
    y=y+"-"*((4*n-3)-x)
    print('-'*((4*n-3)-x),end='')
    lst.append(y)
    print()
print()
for i in range(0,lst.__len__()):
    print(lst[lst.__len__()-1-i])

t=input()
t=int(n)
while t>0:
    n=input()
    n=int(n)
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)
    t=t-1

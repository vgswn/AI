def checks(m, n, a, b):
    if a<m and a>=0:
        if b<n and b>=0:
            return True
    return False


def issafe(grid, count, friend, key, n, m, row, col):
    ver=[[0, 1],[0, -1],[1, 0],[-1, 0],[1, 1],[1, -1],[-1, 1], [-1, -1]]
    for i in range(8):
        if checks(m, n, row+ver[i][0], col+ver[i][1]):
            if grid[row+ver[i][0]][col+ver[i][1]] not in friend[key]:
                return False
    return True



def fill(check, grid, count, friend, n, m, row, col):
    for key in check.keys():
        if check[key]==0 and issafe(grid, count, friend, key, n, m, row, col):
            grid[row][col]=key
            check[key]=1
            if row==m-1 and col==n-1:
                return True
            if col==n-1:
                ret=fill(check, grid, count, friend, n, m, row+1, 0)
            else:
                ret=fill(check, grid, count, friend, n, m, row, col+1)
            if ret:
                return True
            check[key]=0
            grid[row][col]='-'
    return False





m=input()
a=m.strip().split(' ')
m=int(a[0])
n=int(a[1])
count={}
friend={}
check={}
for i in range(m*n):
    c=input().strip().split(' ')
    count[c[0]]=int(c[1])
    check[c[0]]=0
    friend[c[0]]=[]
    for j in range(count[c[0]]):
        friend[c[0]].append(c[j+2])
grid=[]
for i in range(m):
    grid.append([])
    for j in range(n):
        grid[i].append('-')
flag=fill(check, grid, count, friend, n, m, 0, 0)
if flag==True:
    for i in range(m):
        for j in range(n):
            print(grid[i][j], " ")
        print("\n")
else:
    print("Not Possible\n")
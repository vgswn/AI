import copy
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                x=(i,j)
                return x
    return False
def domain_reduce(domain,i,j,board):
    val = board[i][j]
    x=i//3
    x=x*3
    y=j//3
    y=y*3

    for a in range(x,x+3):
        for b in range(y,y+3):
            if a>=9 or b>=9:
                continue
            if domain[a][b].__contains__(val) and (a!=i or b!=j):
                domain[a][b].remove(val)
    for a in range(9):
        if a!=j:
            if domain[i][a].__contains__(val) and a!=j:
                domain[i][a].remove(val)
    for b in range(9):
        if b!=i:
          if domain[b][j].__contains__(val) and b!=i:
                domain[b][j].remove(val)
    for x in range(9):
        for y in range(9):
            if len(domain[x][y]) == 0:
                return False
    return True



def solve_sudoku(board,domain):
    x=find_empty(board)
    if x == False:
        return True
    for i in domain[x[0]][x[1]]:
        board[x[0]][x[1]]=i
        dom1=copy.deepcopy(domain)
        if domain_reduce(dom1,x[0],x[1],board) !=False:
            if solve_sudoku(board,dom1) ==   True:
                return True
        board[x[0]][x[1]]=0
    return False



board=[]
for i in range(9):
    board.append([])
    x=input().split(" ")
    for j in range(9):
        board[i].append(int(x[j]))
domain=[]
for i in range(9):
    domain.append([])
for i in range(9):
    for j in range(9):
        domain[i].append([])
    for j in range(9):
        for k in range(1,10):
            domain[i][j].append(k)
#print(domain[0][0][0])
for i in range(9):
    for j in range(9):
        domain_reduce(domain, j, i, board)
solve_sudoku(board,domain)
for i in range(9):
    print(board[i])
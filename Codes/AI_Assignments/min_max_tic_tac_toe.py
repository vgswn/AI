def score(board,me,d):
    for i in range(3):
        if(board[i][0]==board[i][1] and board[i][1]==board[i][2] and board[i][2]!='_'):
            if(board[i][0]==me):
                return 10-d
            else:
                return -10+d
    for i in range(3):
        if(board[0][i]==board[1][i] and board[1][i]==board[2][i]and board[2][i]!='_'):
            if(board[0][i]==me):
                return 10-d
            else:
                return -10+d
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2]and board[2][2]!='_'):
        if(board[0][0])==me:
            return 10-d
        else :
            return -10+d
    if(board[0][2]==board[1][1] and board[1][1]==board[2][0]and board[2][2]!='_'):
        if(board[0][2])==me:
            return 10-d
        else:
            return -10+d
    return  0

def moves(board):
    for i in range(3):
        for j in range(3):
            if board[i][j]=='_':
                return 1
    return 0
def min_max(board,me,opponent,f,d):
    x=score(board,me,d)
    #print(x)
    if(x!=0):
        return x

    if moves(board)==0:
        #print(board)
        return 0

    if f==0:
        new_score=100
        for i in range(3):
            for j in range(3):
                if board[i][j]=='_':
                    board[i][j]=opponent
                    #print(board)

                    new_score=min(min_max(board,me,opponent,1,d+1),new_score)
                    board[i][j]='_'
        return new_score
    if f==1:
        new_score=-100
        for i in range(3):
            for j in range(3):
                if board[i][j]=='_':
                    board[i][j]=me
                    #print(board)
                    new_score=max(min_max(board,me,opponent,0,d+1),new_score)
                    board[i][j]='_'
        return new_score





me=input()
opponent='o'
if me=='o':
    opponent='x'

board=[]
for i in range(3):
    board.append([])
    x=input()
    for j in range(3):
        board[i].append(x[j])
#print(board)
#print(board[2][2])
#print(me,opponent)
values={}
a=-500
b=(100,100)
for i in range(3):
    for j in range(3):
        #print(i,j)
        if board[i][j]=='_':
            x=(i,j)
            #print(x)
            board[i][j]=me
            q=min_max(board,me,opponent,0,0)
            #print(i,j,q)
            if q>=a:
                a=q
                b=x
            #print(x,values[x])

            board[i][j]='_'

print(b[0],b[1])
#print(max(100,50))
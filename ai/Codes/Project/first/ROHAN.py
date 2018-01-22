import copy
'''
1 win
-1 lose
0 tie
2 not over
'''
def game_over(player,board):
    if player == 'x':
        p1 = 'o'
    else:
        p1='x'
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == player:
            return 1
        elif board[i][0] == board[i][1] and board[i][1] == board[i][2]and board[i][0] == p1:
            return -1
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == player:
            return 1
        elif board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == p1:
            return -1

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == player:
        return 1
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == p1:
        return -1
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == player:
        return 1
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == p1:
        return -1
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                return 2
    return 0

def min_move(player,board):

    g=game_over(player,board)
    if g != 2:
        return g,board
    else :
        val = 10
        prevx =-1
        prevy =-1
        board1=copy.deepcopy(board)
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    if player == 'x':
                        board1[i][j] = 'o'
                    else:
                        board1[i][j] = 'x'
                else:
                    continue

                val1,b1=max_move(player,board1)


                if val > val1:
                    val=val1
                    prevx = i
                    prevy = j
                board1 = copy.deepcopy(board)
        if player == 'x':
            board[prevx][prevy]='o'
        else:
            board[prevx][prevy] = 'x'

        return val,board

def max_move(player,board):
    g=game_over(player,board)
    if g != 2:
        return g,board
    else :
        val = -100
        prevx = -1
        prevy = -1
        board1 = copy.deepcopy(board)
        for i in range(3):
            for j in range(3):
                if board1[i][j] == '_':
                    board1[i][j] = player
                else:
                    continue


                val1, b1 = min_move(player, board1)

                if val < val1:
                    val=val1
                    prevx = i
                    prevy = j
                board1 = copy.deepcopy(board)
        board[prevx][prevy]=player

        return val,board


x=input()
board=[]
for i in range(3):
    b=[]
    s=input()
    y,y1,y2=[i for i in s]
    b.append(y)
    b.append(y1)
    b.append(y2)
    board.append(b)
val,board=max_move(x,board)

for i in range(3):
    print(board[i])
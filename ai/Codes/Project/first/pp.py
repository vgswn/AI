import random
import queue as q

def RULE_MATCH(matrix, x, y, count, n, m, visited_cell):

    d = q.PriorityQueue()
    if x-1 >=0 and visited_cell[x-1][y]==0:
        if matrix[x-1][y]=='Dirty':
            d.put([1+(-5),'UP'])
        else :
            d.put([1,'UP'])
    if x+1< n and visited_cell[x+1][y]==0 :
        if matrix[x+1][y]=='Dirty':
            d.put([2+(-5),'DOWN'])
        else :
            d.put([2,'DOWN'])
    if y-1 >=0 and visited_cell[x][y-1]==0 :
        if matrix[x][y-1]=='Dirty':
            d.put([3+(-5),'LEFT'])
        else :
            d.put([3,'LEFT'])
    if y+1 < m and visited_cell[x][y+1]==0:
        if matrix[x][y+1]=='Dirty':
            d.put([4+(-5),'RIGHT'])
        else :
            d.put([4,'RIGHT'])
    if d.empty() :
        flag = 0
        while flag == 0:
            r = random.randrange(4)
            if r == 0 and x - 1 >= 0:
                flag = 1
                return 'UP'
            elif r == 1 and x + 1 <= n:
                flag = 1
                return 'DOWN'
            elif r == 2 and y - 1 >= 0:
                flag = 1
                return 'LEFT'
            elif r == 3 and y + 1 <= m:
                flag = 1
                return 'RIGHT'
    x=d.get()
    return x[1]






def SIMPLE_REFLEX_AGENT(matrix, x, y, count, n, m, visited_cell):
    if matrix[x][y] == 'Dirty':
        matrix[x][y] = 'Clean'
        print('Sucked at ', x, y)


    return RULE_MATCH(matrix, x, y, count, n, m, visited_cell)


def vacuum_cleaner(matrix, x, y, count, n, m, visited_cell):
    if count == (m + 1) * (n + 1):
        return
    if visited_cell[x][y] == 0:
        count = count + 1

    visited_cell[x][y] = 1
    action = SIMPLE_REFLEX_AGENT(matrix, x, y, count, n, m, visited_cell)
    if action == 'UP':
        print('going up from ', x, y, ' to ', x - 1, y)
        vacuum_cleaner(matrix, x - 1, y, count, n, m, visited_cell)

    elif action == 'DOWN':
        print('going down from ', x, y, ' to ', x + 1, y)
        vacuum_cleaner(matrix, x + 1, y, count, n, m, visited_cell)
    elif action == 'LEFT':
        print('going left from ', x, y, ' to ', x, y - 1)
        vacuum_cleaner(matrix, x, y - 1, count, n, m, visited_cell)
    elif action == 'RIGHT':
        print('going right from ', x, y, ' to ', x, y + 1)
        vacuum_cleaner(matrix, x, y + 1, count, n, m, visited_cell)

n, m = input().split(' ')
n, m = (int(n), int(m))
matrix = []
visited_cell = []
for i in range(n):
    matrix.append([])
    visited_cell.append([])
    for j in range(m):
        x = random.randrange(2)
        visited_cell[i].append(0)
        if x == 0:
            matrix[i].append('Clean')
        else:
            matrix[i].append('Dirty')
print(matrix)
x = random.randrange(n)
y = random.randrange(m)
count = 0
vacuum_cleaner(matrix, x, y, count, n - 1, m - 1, visited_cell)
print(visited_cell)


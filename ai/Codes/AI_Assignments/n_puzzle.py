import queue as qu
import copy


def hn(front, n, for_h):
    count = 0;
    for i in range(n):
        for j in range(n):
            x = for_h[front[i][j]]
            count = count + abs(x[0] - i) + abs(x[1] - j)

    return count

def h2n(front,n,final):
    count=0
    for i in range(n):
        for j in range(n):
            if front[i][j]==final[i][j]:
                count=count+1
    return count
def n_puzzle(init, final, vis, n, for_h, par):
    a = 0
    pq = qu.PriorityQueue()
    front = init
    x = hn(front, n, for_h)
    x=h2n(front,n,final)
    x=x*(-1)
    print(x)
    pq.put((x, init))
    vis.append(init)
    par[tuple(tuple(x) for x in init)] = 'EXIT'
    while not pq.empty():
        a = 0
        # print(pq.queue)
        new = pq.get()
        front = new[1]
        p = new[0]


        # print(front)
        if (p == -9):
            # print('found')
            break

        for i in range(n):
            for j in range(n):
                if front[i][j] == 0:
                    x = i
                    y = j
        cs = copy.deepcopy(front)
        if x - 1 >= 0:
            cs[x - 1][y], cs[x][y] = cs[x][y], cs[x - 1][y]
            if vis.__contains__(cs) == False:
                vis.append(cs)
                c = hn(cs, n, for_h)
                c=h2n(cs,n,final)
                c=c*(-1)
                pq.put((c, cs))
                par[tuple(tuple(x) for x in cs)] = (front, 'UP')

        cs = copy.deepcopy(front)
        if x + 1 < n:
            cs[x + 1][y], cs[x][y] = cs[x][y], cs[x + 1][y]
            if vis.__contains__(cs) == False:
                vis.append(cs)
                c = hn(cs, n, for_h)
                c=h2n(cs,n,final)
                c=c*(-1)
                pq.put((c, cs))
                par[tuple(tuple(x) for x in cs)] = (front, 'DOWN')

        cs = copy.deepcopy(front)
        if y + 1 < n:
            cs[x][y + 1], cs[x][y] = cs[x][y], cs[x][y + 1]
            if vis.__contains__(cs) == False:
                vis.append(cs)
                c = hn(cs, n, for_h)
                c=h2n(cs,n,final)
                c=c*(-1)
                pq.put((c, cs))
                par[tuple(tuple(x) for x in cs)] = (front, 'RIGHT')

        cs = copy.deepcopy(front)
        if y - 1 >= 0:
            cs[x][y - 1], cs[x][y] = cs[x][y], cs[x][y - 1]
            if vis.__contains__(cs) == False:
                vis.append(cs)
                c = hn(cs, n, for_h)
                c=h2n(cs,n,final)
                c=c*(-1)
                pq.put((c, cs))
                par[tuple(tuple(x) for x in cs)] = (front, 'LEFT')


def printf(c, final, par):
    c = c + 1
    x = par[tuple(tuple(x) for x in final)]
    if x == 'EXIT':
        print(c - 1)
        return
    else:

        printf(c, x[0], par)
        print(x[1])


n = int(input())
init = []
for i in range(n):
    init.append([])
    for j in range(n):
        init[i].append(int(input()))

final = []
x = 0
for i in range(n):
    final.append([])
    for j in range(n):
        final[i].append(x)
        x = x + 1
for_h = {}
for i in range(n):
    for j in range(n):
        for_h[final[i][j]] = (i, j)
vis = []
par = {}

n_puzzle(init, final, vis, n, for_h, par)
c = 0
printf(c, final, par)




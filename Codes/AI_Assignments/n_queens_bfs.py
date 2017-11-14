import queue
import copy
def is_safe(new,row,column,n):
    for i in range (n):

        if new[row][i]==1:
            return False
    for i in range (n):

        if new[i][column]==1:
            return False
    i=row
    j=column
    while i>=0 and j>=0:
            if new[i][j]==1:
                return False
            i=i-1
            j=j-1
    i=row
    j=column
    while i<n and j>=0:
            if new[i][j]==1:
                return False
            i=i+1
            j=j-1
    i=row
    j=column
    while i<n and j<n:
            if new[i][j]==1:
                return False
            i=i+1
            j=j+1
    i=row
    j=column
    while i>=0 and j<n:
            if new[i][j]==1:
                return False
            i=i-1
            j=j+1
    return True




def is_goal(new,n):
    for i in range (n):
        count=0
        for j in range(n):
            if new[i][j]==1:
                count=count+1
        if count!=1:
            return False
    return True

def bfs(Matrix,n):
    pq=queue.Queue()
    pq.put((Matrix,0))
    f=0
    m=Matrix
    while not pq.empty():
        m,x=pq.get()
        #print(m)

        for i in range(n):
            #print(x)
            new=copy.deepcopy(m)
            #print(m)
            if is_safe(new,i,x,n)==True:
                new[i][x] = 1
                #print(new)
                pq.put((new,x+1))
                #print('these two')
                #print(m)
                #print(new)
                #print()
                if is_goal(new,n)==True:
                    print(new)
                    f=1
                    break



        if f==1:
             break
    #print(m)





n=int(input())
Matrix = [[0 for x in range(n)] for y in range(n)]
bfs(Matrix,n)

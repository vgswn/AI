import queue
def is_safe(graph,map,index,i,final):

    f=True
    for j in graph[index]:
      if final[j]==color[i]:
            f=False
            break
    return f
def find_options(graph, final, map,color):
    min_value=100
    min_map=''
    for i in range(len(map)):
        count = 1000
        if final[map[i]]==color[0]:
            count=0
            for j in range(1,4):
                if is_safe(graph,map,map[i],j,final)==True:
                    count=count+1
        if min_value > count:
            min_value=count
            min_map=map[i]
        if min_value == count:
            if len(graph[map[i]]) > len(graph[min_map]):
                min_value = count
                min_map = map[i]

    #print(min_value)
    return min_map
def find_options2(graph,final,map,c,p,color):
    x=final[p]
    final[p]=color[c]
    count=0
    for i in range(len(map)):
        if final[map[i]] == color[0]:
                for index in range(1,4):
                    if is_safe(graph, map, map[i], index, final)==True:
                        count=count+1
    final[p]=x
    return count



def is_goal(final):
    c=0
    for i in final:
       if final[i]!=color[0]:
           c=c+1
    if c==len(final)+1:
        return True
    return False

def map_coloring(graph,map,final,color):
    if is_goal(final)==True :
        return True



    x=find_options(graph, final, map,color)
    if x=='':
        return True
    #print(x)
    pq = queue.PriorityQueue()
    for i in range(1,4):

        xx = find_options2(graph, final, map, i, x, color)
        pq.put((-1*xx, i))
    while pq.empty()!=True:
        q=pq.get()
        i=q[1]
        #print(x,i)

        if is_safe(graph,map,x,i,final)==True:
            final[x]=color[i]

            if map_coloring(graph,map,final,color)==True:
                  return True
            final[x]=color[0]
    return False





graph={'Western Australia':('Nothern Teritory','South Australia'),
       'Nothern Teritory':('Western Australia','South Australia','Queensland'),
       'South Australia':('Western Australia','Nothern Teritory','Queensland','New South Wales','Victoria'),
       'Queensland':('Nothern Teritory','South Australia','New South Wales'),
       'New South Wales':('South Australia','Queensland','Victoria'),
       'Victoria':('South Australia','New South Wales'),'Tasmania':()
    }
map=[]
for i in graph.keys():
    map.append(i)

color={}
color[0]='RGB'
color[1]='Red'
color[2]='Green'
color[3]='Blue'
final={}
for i in map:
    final[i]='RGB'


map_coloring(graph,map,final,color)
'''for i in map:
    print(i,final[i],':',end=' ')
    for j in graph[i]:
        print(j,final[j],end=' , ')
    print('')'''
for i in map:
    a=0
    print(i,':',final[i])


import queue
def is_safe(graph,map,index,i,final):

    f=True
    for j in graph[map[index]]:
      if final[j]==color[i]:
            f=False
            break
    return f
def find_options(graph,final,map,c,p,color):
    x=final[p]
    final[p]=color[c]
    count=0
    for i in range(len(map)):
        if final[map[i]] == color[0]:
                for index in range(1,4):
                    if is_safe(graph, map, i, index, final)==True:
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

def map_coloring(graph,map,final,index):
    if is_goal(final)==True or index==len(map):
        return True
    a=0
    pq=queue.PriorityQueue()

    for i in range(1,4):
        x=find_options(graph, final, map, i, map[index], color)
        pq.put((x,i))
    while pq.empty()!=True:

        q=pq.get()
        i=q[1]

        if is_safe(graph,map,index,i,final)==True:
            final[map[index]]=color[i]

            if map_coloring(graph,map,final,index+1)==True:
                  return True
            final[map[index]]=color[0]
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


map_coloring(graph,map,final,0)
'''for i in map:
    print(i,final[i],':',end=' ')
    for j in graph[i]:
        print(j,final[j],end=' , ')
    print('')'''
for i in map:
    print(i,':',final[i])


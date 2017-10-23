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



def is_goal(final):
    c=0
    for i in final:
       if final[i]!=color[0]:
           c=c+1
    if c==len(final)+1:
        return True
    return False
def domain_reduction(graph,map,final,domain):
    for i in map:
        x=[]
        for j in range(1,4):
            if is_safe(graph, map, i, j, final) == True:
                x.append(j)
        domain[i]=x
def map_coloring(graph,map,final,color,domain):
    if is_goal(final)==True :
        return True



    x=find_options(graph, final, map,color)
    if x=='':
        return True
    #print(x)
    domain_reduction(graph,map,final,domain)
    for i in domain[x]:

            final[x]=color[i]


            if map_coloring(graph,map,final,color,domain)==True:
                  return True
            final[x]=color[0]
            domain_reduction(graph, map, final, domain)
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

domain={}
for i in graph.keys():
    x=(1,2,3)
    domain[i]=x
#print(domain)

map_coloring(graph,map,final,color,domain)
'''for i in map:
    print(i,final[i],':',end=' ')
    for j in graph[i]:
        print(j,final[j],end=' , ')
    print('')'''
for i in map:
    a=0
    print(i,':',final[i])
#print(domain)


import queue
def h_sld(SLDip,q):
    return SLDip[q]

def a_star(SLDip,graph,source,dest,parent):
    a=0
    vis=[]
    d={}

    vis.append(source)
    parent[source]='EXIT'
    pq=queue.PriorityQueue()
    x=h_sld(SLDip,source)
    pq.put((x,source,0))
    d[source]=0
    while not pq.empty():
        front=pq.get()
        new=front[1]
        h=front[0]
        f=front[2]
        vis.append(new)
        if new=='Bucharest':

            print('Distance From ',source,'to ',new,'is ',f)
            break

        neigh=graph[new]
        #print(neigh)
        for i in range (len(neigh)):

            p=neigh[i]
            g = f + p[1]

            if vis.__contains__(p[0])==False  :
                #print(p)
                if d.__contains__(p[0]):
                    if d[p[0]] < g :
                        continue
                h=h_sld(SLDip,p[0])

                fn=h+g
                #print(fn)
                pq.put((fn,p[0],g))
                parent[p[0]]=new




def printf(final,parent):
    if parent[final]=='EXIT':
        print(final,end='')
        return
    else:
        printf(parent[final],parent)
        print('->',final,end='')


SLDip = {'Arad':366,
         'Bucharest':0,
         'Craiova': 160,
         'Drobeta': 242,
         'Eforie' : 161,
         'Fagaras' : 176,
         'Giurgiu':77,
         'Hirsova':151,
         'Iasi': 226,
         'Lugoj': 244,
         'Mehadia': 241,
         'Neamt': 234,
         'Oradea': 380,
         'Pitesti': 100,
         'Rimnicu Vilcea': 193,
         'Sibiu': 253,
         'Timisoara': 329,
         'Urziceni': 80,
         'Vaslui': 199,
         'Zerind': 374}

graph = {'Oradea': [('Zerind', 71), ('Sibiu',151)],
         'Zerind': [('Oradea', 71), ('Arad', 75)],
         'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
         'Timisoara': [('Arad', 118), ('Lugoj', 111)],
         'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
         'Mehadia': [('Lugoj', 70), ('Drobeta', 75)],
         'Drobeta': [('Mehadia', 75), ('Craiova',120)],
         'Sibiu': [('Oradea', 151), ('Arad', 140), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
         'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
         'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
         'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
         'Giurgiu': [('Bucharest', 90)],
         'Bucharest': [('Fagaras',211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni',85)],
         'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
         'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
         'Iasi': [('Vaslui', 92), ('Neamt', 87)],
         'Neamt': [('Iasi', 87)],
         'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
         'Eforie': [('Hirsova', 86)],
         'Craiova':[('Drobeta',120),('Rimnicu Vilcea',146),('Pitesti',138)]

         }
#print(len(graph))
i=1
for key,value in SLDip.items():
    print(i,key)
    i=i+1;
parent={}
for inp,x in graph.items():
    a_star(SLDip,graph,inp,'Bucharest',parent)
print('Path is ')
printf('Bucharest',parent)

import queue
def input_from_file(SLDip,Dict):

    f = open("SLDip",'r')

    for i in range(20):
        a=f.readline()
        x,y=a.split(",")
        SLDip[x]=int(y)
    #print(SLDip)
    f.close()
    with open('Dict','r') as myfile:
        count = sum(1 for line in myfile)
    f=open('Dict','r')
    #print(count)
    #Dict={}
    for i in range(count):
        a=f.readline()


        x,y=a.split(":")
        q=y.split(",")
    #print(q)
        new=[]
        for j in range(len(q)):
            s=q[j].split(" ")
            a=(s[0],int(s[1]))
            new.append(a)
        Dict[x]=new
    #print(Dict)
def h_sld(SLDip,q):
    return SLDip[q]

def a_star(SLDip,graph,source,dest,parent):
    ff=open('output','a+')

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
            a=0
            ff.write('Distance From '+str(source)+'to '+str(new)+'is '+ str(f))
            ff.write('\n')
            #print()
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
                d[p[0]]=g




def printf(final,parent):
    if parent[final]=='EXIT':
        print(final,end='')
        return
    else:
        printf(parent[final],parent)
        print('->',final,end='')

f=open('output','w')
f.close()
SLDip={}
graph={}
input_from_file(SLDip,graph)
i=1
'''for key,value in SLDip.items():
    print(i,key)
    i=i+1;'''
parent={}
for inp,x in graph.items():
    a_star(SLDip,graph,inp,'Bucharest',parent)
parent={}
#a_star(SLDip,graph,'Zerind','Bucharest',parent)
'''print('Path is ')
printf('Bucharest',parent)'''







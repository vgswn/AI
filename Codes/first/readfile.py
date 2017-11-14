f=open('read','r')
for line in f:
    #print(line,end='')
    line=line.split(sep=' ')
    print(line)
f.close()
f=open('read','w')
f.write("writing to file")
f.close()
p="Hey python"
p=p.split(sep=' ')
print(p)

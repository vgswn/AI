f=open("test.txt","r")
list=[]
for line in f:
    print(line)
    list.append(line)
print(list)
f.close()
f=open("test.txt","a")
f.write('\n')
for a in list:
    f.write(a)

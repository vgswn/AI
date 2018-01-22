class stack:
    def __init__(self,arr):
            self.arr=[]
    def push(self,x):
        self.arr.append(x)
    def pop(self):
        x=self.arr[self.arr.__len__()-1]
        self.arr.pop()
        return self.arr
    def top(self):
        return self.arr[self.arr.__len__()-1];

class queue:
    def __init__(self,arr):
        self.arr=[]
    def enqueue(self,x):
        self.arr.append(x)
    def deque(self):
        x=self.arr[0]
        self.arr.remove(self.arr[0])
        return self.arr
    def front(self):
        return self.arr[0];

class hashmap:
    def __init__(self,arr):
        self.arr=dict()
    def add(self,x,y):
        self.arr[x]=y
    def getvalue(self,x):
        return self.arr.get(x)
    def remove(self,x):
        if self.arr.__contains__(x):
            del self.arr[x]

var=stack([])
var.push("abcd");
var.push("bacd");
var.push("ffd");
print(var.arr)
print(var.pop())
print(var.arr)
print(var.top())


ob=queue([])
ob.enqueue(1)
ob.enqueue(2)
ob.enqueue(3)
print(ob.arr)
print(ob.deque())
print(ob.arr)
print(ob.front())


a=hashmap({})
a.add("abc",1)
a.add("bcd",2)
a.add("cde",3)
print(a.arr)
a.remove("abc")
print(a.arr)
print(a.getvalue("cde"))
a.remove("abc")
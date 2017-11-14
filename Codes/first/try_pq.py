import queue as q
class my:
    def __init__(self,a,b):
        self.first=a
        self.second=b
    def __lt__(self,other):
        if self.first!=other.first:
            return self.first > other.first
        else:
            return self.second < other.second
pq=q.PriorityQueue()
pq.put([[1,2],3])
pq.put([[3,4],5])
print(pq.get(),pq.get())

pq.put(my(10,3))
pq.put(my(3,4))
pq.put(my(3,6))
print(pq.get().first,pq.get().second)

s=set()
s.add(100)
s.add(10)
s.add(10)
print(s)

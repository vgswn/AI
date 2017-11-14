import queue
pq=queue.PriorityQueue()
pq.put((10,20,3))
pq.put((3,4,5))
print(pq.get())
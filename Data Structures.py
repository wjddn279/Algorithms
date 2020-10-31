class MyList:
    def __init__(self):
        self.List = []

    def push(self, num):
        self.List = self.List +[num]

    def pop(self):
        if self.List:
            temp = self.List[-1]
            self.List = self.List[0:len(self.List)-1]
            return temp
        else:
            return -1

    def print(self):
        print(self.List)

import heapq

class MyHeap:
    def __init__(self,arr=[]):
        self.heapfy(arr)

    def heapfy(self,arr):
        self.arr = arr
        total = len(self.arr)
        for idx,num in enumerate(self.arr):
            left,right = 2*idx+1,2*idx+2
            if left < total and self.arr[idx] > self.arr[left]:
                self.arr[idx],self.arr[left] = self.arr[left], self.arr[idx]
            if right < total and self.arr[idx] > self.arr[right]:
                self.arr[idx],self.arr[right] = self.arr[right],self.arr[idx]

    def heappush(self,a):
        self.arr.append(a)
        now = len(self.arr)-1
        next = (now-1)//2
        while self.arr[now] < self.arr[next]:
            if now == 0:
                break
            self.arr[now],self.arr[next] = self.arr[next],self.arr[now]
            now = next
            next = (now-1)//2
        print(self.arr)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def add(self,node):
        if self.next is None:
            self.next = node
        else:
            n = self.next
            while n.next is None:
                n.next = node
                break
            else:
                n = n.next
    def select(self,idx):
        n = self.next
        for i in range(idx-1):
            n = n.next
        return n.data

class linkedList:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

a = linkedList(3,linkedList(4))
print(a.next.data)



a = [4,7,1,3,10]
heapq.heapify(a)
heapq.heappush(a,1)
print(a)
heapq.heappop(a)
print(a)
heap = MyHeap([4,7,1,3,10])
heap.heappush(1)

arr = [1,1]


class MyList():
    def __init__(self):
        self.List = []

    def push(self, num):
        self.List = self.List +[num]

    def pop(self):
        print(self.List)
        self.List = self.List[0:len(self.List)-1]
        print(self.List)
    def prin(self):
        print(self.List)


def BubbleSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(i,length):
            if arr[i] < arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr


# def HeapSort(arr):
#     length = len(arr)
#     for i in range(length):


def QuickSort(arr):
    if len(arr) <= 1 : return arr
    pivot = arr[len(arr)//2-1]
    prior,equal,post = [], [], []
    for num in arr:
        if num < pivot: prior.append(num)
        elif num > pivot: post.append(num)
        else: equal.append(num)
    return QuickSort(post)+equal+QuickSort(prior)



arr = [7,3,2,9,4]
print(BubbleSort(arr))
print(QuickSort(arr))
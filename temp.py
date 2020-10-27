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


def memozation(n):
    dp[1],dp[2] = 1,1
    if dp[n]:
        return dp[n]
    dp[n] = memozation(n-1)+memozation(n-2)
    return dp[n]

def up(n):
    if n <= 2:
        return 1
    dp = [0,1,1]
    for i in range(3,n+2):
        dp.append(dp[i-1]+dp[i-2])
    return dp[n]

print(up(10))




dp = [0 for _ in range(11)]
print(memozation(10))
print(dp)


# arr = [7,3,2,9,4]
# print(BubbleSort(arr))
# print(QuickSort(arr))
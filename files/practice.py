import heapq

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()
a = [[1,2,3],[4,5,6],[7,8,9]]
prin(a)
for i in range(len(a)):
    for j in range(i+1,len(a[0])):
        a[i][j],a[j][i] = a[j][i],a[i][j]
prin(a)


a = [(2,1),(1,3),(3,6)]
heapq.heapify(a)

print(a)

a = [0]
b = [0]
print(a+b)
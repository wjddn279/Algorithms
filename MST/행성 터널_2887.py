import sys
sys.stdin = open("../input.txt")

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    fx,fy = find(x),find(y)
    if fx != fy:
        parent[fy] = fx
        return True
    else:
        return False

N = int(input())
data = [list(map(int,input().split()))+[i] for i in range(N)]
sorted_data = [sorted(data,key=lambda x:x[i]) for i in range(3)]

tree = []
for idx,sd in enumerate(sorted_data):
    for i in range(len(sd)-1):
        tree.append([abs(sd[i][idx]-sd[i+1][idx]),sd[i][3],sd[i+1][3]])

tree.sort()
parent = [i for i in range(N+1)]
result = 0
for cost,x,y in tree:
    if union(x,y):
        result += cost

print(result)
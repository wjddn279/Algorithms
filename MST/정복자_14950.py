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

N,M,T = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(M)]
data.sort(key=lambda x:x[2])
parent = [i for i in range(N+1)]

result,time = 0, 0
for x,y,cost in data:
    if union(x,y):
        result += cost+ time * T
        time += 1
print(result)
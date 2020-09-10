import sys
sys.stdin = open("../input.txt")


def find(x):
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x,y):
    fx,fy = find(x),find(y)
    if fx != fy:
        parents[fy] = fx
        return True
    else:
        return False

V, E = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(E)]
data.sort(key= lambda x:x[2])
parents = [i for i in range(V+1)]
result = 0
for x,y,cost in data:
    if union(x,y):
        result += cost
print(result)


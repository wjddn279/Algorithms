elements = [0,1,2,3,2,5,6,4,8,9,10]

parent = [element for element in elements]

def find(n):
    if n == parent[n]:
        return n
    parent[n] = find(parent[n])
    return parent[n]

def union(a,b):
    root_a = find(a)
    root_b = find(b)

    if root_a != root_b:

        parent[root_b] = root_a

V, E = map(int,input().split())
data = [[] for _ in range(V)]
node = [i for i in range(V)]

for i in range(E):
    a,b,c = map(int,input().split())
    data[a].append((b,c))
    

import sys
sys.stdin = open("input7.txt")

def dji(min_node):
    visited = [0 for _ in range(V + 1)]
    visited[0] = 1

    distance = [float('inf') for _ in range(V + 1)]
    distance[min_node] = 0

    while True:
        for arrive, cost in data[min_node]:
            if visited[arrive] == 0:
                via = distance[min_node] + cost
                if via < distance[arrive]:
                    distance[arrive] = via

        visited[min_node] = 1
        min_value = float('inf')

        for i in range(1, V + 1):
            if distance[i] < min_value and visited[i] == 0:
                min_value = distance[i]
                min_node = i

        if visited[min_node]:
            return distance

V, E = map(int,input().split())
min_node = int(input())

data = [[] for _ in range(V+1)]
for i in range(E):
    a,b,c = map(int,input().split())
    data[a].append((b,c))

distance = dji(min_node)

for i in range(1,len(distance)):
    if distance[i] == float('inf'):
        print("INF")
    else:
        print(distance[i])

import sys
sys.stdin = open("party_1238.txt")

import heapq


def search(start_point, end_point):
    distance = [float('inf') for _ in range(N + 1)]
    distance[start_point] = 0

    visited = [0 for _ in range(N + 1)]
    visited[start_point] = 1

    heap = []
    heapq.heappush(heap, (0, start_point))

    while heap:
        dis, location = heapq.heappop(heap)
        if location == end_point:
            break
        for arrive, cost in graph[location]:
            candidate = dis + cost
            if candidate < distance[arrive]:
                distance[arrive] = candidate
                heapq.heappush(heap, (distance[arrive], arrive))

    return distance[end_point]

N, M ,end_point = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int,input().split())
    graph[start].append((end,cost))

result = 0

for i in range(1,N+1):
    temp = 0
    if i == end_point:
        continue
    temp = temp + search(i,end_point) + search(end_point,i)
    result = max(result,temp)

print(result)
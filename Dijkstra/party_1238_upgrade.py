import sys
sys.stdin = open("party_1238.txt")

import heapq


def search(start_point, graph):
    distance = [float('inf') for _ in range(N + 1)]
    distance[start_point] = 0

    heap = []
    heapq.heappush(heap, (0, start_point))

    while heap:
        dis, location = heapq.heappop(heap)
        if distance[location] < dis:
            continue
        for arrive, cost in graph[location]:
            candidate = dis + cost
            if candidate < distance[arrive]:
                distance[arrive] = candidate
                heapq.heappush(heap, (distance[arrive], arrive))

    return distance

N, M ,end_point = map(int,input().split())
path = [[] for _ in range(N+1)]
reverse = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int,input().split())
    path[start].append((end,cost))
    reverse[end].append((start,cost))

dis = search(end_point,path)
rev_dis = search(end_point,reverse)
result = 0
for i in range(1,N+1):
    result = max(result,dis[i]+rev_dis[i])

print(result)
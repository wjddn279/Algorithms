import heapq
import sys
sys.stdin = open("input7.txt")

T = int(input())

for test_case in range(1,T+1):
    V, E  = map(int,input().split())
    data = [[] for _ in range(V)]
    for _ in range(E):
        a,b,c = map(int,input().split())
        data[a].append((b,c))
    distance = [float('inf') for _ in range(V+1)]
    distance[0] = 0

    heap = []
    heapq.heappush(heap,(0,0))
    while heap:
        dis, location = heapq.heappop(heap)
        if location == V:
            break
        for arrive,cost in data[location]:
            candidate = dis + cost
            if candidate < distance[arrive]:
                distance[arrive] = candidate
                heapq.heappush(heap,(distance[arrive],arrive))

    print('#{} {}'.format(test_case,distance[V]))
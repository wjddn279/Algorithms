import sys
sys.stdin = open("../input.txt")

def prin(a):
    for i in a:
        print(*i)
    print()

import heapq
from _collections import deque

while True:
    N,M = map(int,input().split())
    if N == 0 and M == 0:
        break
    start, end = map(int,input().split())
    data = [[] for _ in range(N)]
    rev_data = [[] for _ in range(N)]
    for _ in range(M):
        x,y,z = map(int,input().split())
        data[x].append((y,z))
        rev_data[y].append((x,z))

    distance = [float('inf') for _ in range(N)]
    distance[start] = 0
    heap = []
    heapq.heappush(heap,(0,start))
    while heap:
        dis,locate = heapq.heappop(heap)
        for arrive,cost in data[locate]:
            if cost + dis < distance[arrive]:
                distance[arrive] = cost + dis
                heapq.heappush(heap,(cost+dis,arrive))

    bound = distance[end]
    block = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append(end)
    while queue:
        now = queue.popleft()
        if now == start:
            continue
        for arrive,cost in rev_data[now]:
            if distance[now] == distance[arrive] + cost:
                block[arrive][now] = 1
                queue.append(arrive)

    next_distance = [float('inf') for _ in range(N)]
    heap = []
    heapq.heappush(heap,(0,start))
    next_distance[start] = 0
    result = -1
    while heap:
        dis,locate = heapq.heappop(heap)
        if locate == end:
            result = dis
            break
        for arrive,cost in data[locate]:
            if cost + dis < next_distance[arrive] and not block[locate][arrive]:
                if arrive == end and cost+dis <= bound:
                    continue
                next_distance[arrive] = cost + dis
                heapq.heappush(heap,(cost+dis,arrive))
    print(result)

import heapq

def solution(n, s, a, b, fares):
    data = [[] for _ in range(n+1)]
    for start,arrive,cost in fares:
        data[start].append((arrive,cost))
        data[arrive].append((start,cost))
    distance = [float('inf') for _ in range(n+1)]
    distance[s] = 0
    heap = []
    heapq.heappush(heap,(0,s))
    while heap:
        dis,location = heapq.heappop(heap)
        for arrive, cost in data[location]:
            temp = dis + cost
            if temp < distance[arrive]:
                distance[arrive] = temp
                heapq.heappush(heap,(distance[arrive],arrive))
    min_val = float('inf')
    for now in range(1,n+1):
        k = distance[now]
        new = [float('inf') for _ in range(n+1)]
        new[now] = 0
        heap = []
        heapq.heappush(heap, (0, now))
        while heap:
            dis, location = heapq.heappop(heap)
            for arrive, cost in data[location]:
                temp = dis + cost
                if temp < new[arrive]:
                    new[arrive] = temp
                    heapq.heappush(heap, (new[arrive], arrive))
        k += new[a]
        k += new[b]
        if k < min_val:
            min_val = k

    return min_val

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
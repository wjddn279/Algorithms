import heapq

def solution(N, road, K):
    answer = 0
    data = [[] for _ in range(N+1)]
    for x,y,c in road:
        data[x].append((y,c))
        data[y].append((x,c))
    heap = []
    distance = [float('inf') for _ in range(N+1)]
    distance[1] = 0
    heapq.heappush(heap,(1,0))
    while heap:
        now,dis = heapq.heappop(heap)
        for arrive,cost in data[now]:
            if distance[arrive] > dis+cost:
                distance[arrive] = dis+cost
                heapq.heappush(heap,(arrive,dis+cost))
    for num in distance:
        if num != float('inf') and num <= K:
            answer += 1

    return answer

print(solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3))
import heapq

def solution(n, edge):
    answer = 0
    data = [[] for _ in range(n+1)]
    for x,y in edge:
        data[x].append((y,1))
        data[y].append((x,1))

    distance = [float('inf') for _ in range(n+1)]
    distance[1] = 0
    max_value,stack = 0, []
    heapq.heappush(stack,(0,1))

    while stack:
        dis,now = heapq.heappop(stack)

        for arrive,cost in data[now]:
            if dis+cost < distance[arrive]:
                distance[arrive] = dis+cost
                heapq.heappush(stack,(cost+dis,arrive))
                if distance[arrive] > max_value:
                    answer = 1
                    max_value = distance[arrive]
                elif distance[arrive] == max_value:
                    answer += 1
    return answer


print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
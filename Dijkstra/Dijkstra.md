# Dijkstra

- 다익스트라 알고리즘이란 ? -> 간선 비용이 음수가 아닌 그래프 상의 한 정점에서 나머지 정점 까지의 최단 거리를 구하는 알고리즘 
- 예를 들면,  A 에서 E 까지 가려하는데 A, B, C, D, E 각각을 연결한 경로의 거리가 1로 같은게 아닌 모두가 다를 때 최소의 비용으로 도달하는 경로를 탐색

0. 간선 정보를 인접 리스트 형태로 저장

```python
# data[i] -> i번 지점에서 출발하여 도착 할 수 있는 지점과 그 경로의 비용 정보들 저장
data = [[] for _ in range(V+1)]
for _ in range(E):
    start, end, cost = map(int,input().split())
    data[start].append((end ,cost))
```

1. 시작 정점에서 각 정점까지 최단 거리를 저장할 메모리를 할당한다.

```python
# 각각의 거리를 저장, 시작점의 거리는 당연히 0
distance = [float('inf') for _ in range(V + 1)]
distance[start] = 0
# 방문 체크, idx를 맞춰 주기 위해 0~v까지 만들어놓고 0은 1로 만듬
visited = [0 for _ in range(V + 1)]
visited[0] = 1
```
2. 시작 정점에서 갈 수 있는 정점들 중 방문한 적이 없고 가장 거리가 가까운 정점 선택.

```python
for _ in range(V+1):
    min_value = float('inf')
    min_node = 0
    for i in range(1,V+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            min_node = i
    visited[i] = 1
```

3. 선택된 정점에서 갈 수 있는 각 다음 정점들에 대해 

- 현재 알려진 최단거리
- 선택된 정점까지의 최단거리 + 선택된 정점에서 다음 정점까지의 거리

   중 가까운 거리로 최단거리를 갱신한다.

```python
	for arrive,cost in data[min_node]:
        distance[arrive] = min(distance[arrive],min_value+cost)
```



- 일반 다익스트라 알고리즘

```python
V, E = map(int,input().split())
data = [[] for _ in range(V+1)]
for _ in range(E):
    start,end,cost = map(int,input().split())
    data[start].append((end,cost))
start_point = int(input())

distance = [float('INF') for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

distance[start_point] = 0

for _ in range(V+1):
    min_value = float('INF')
    min_node = 0
    for i in range(1,V+1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            min_node = i
            
	visited[min_node] = 1
    
    for arrive,cost in data[min_node]:
        distance[arrive] = min(distance[arrive], distance[min_node]+cost)

print(distance)
```

- heap을 활용한 다익스트라

```python
import heapq

V, E = map(int,input().split())
data = [[] for _ in range(V+1)]
for _ in range(E):
    start,end,cost = map(int,input().split())
    data[start].append((end,cost))
    
start_point = int(input())

distance = [float('INF') for _ in range(V+1)]
visited = [0 for _ in range(V+1)]

distance[start_point] = 0

heap = []
heapq.heappush(heap,(0,start_point))

while heap:
    # heap 중 dis가 가장 작은 dis, location이 pop 됨
    # dis : start_point에서 location까지 현재 최단 거리
    dis, location = heapq.heappop(heap)
    if location == end_point:
        break
    for arrive, cost in data[location]:
        candidate = dis + cost
        if candidate < distance[arrive]:
            distance[arrive] = candidate
            heapq.heappush(heap,(distance[arrive],arrive))
```


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
            min_value
```

3. 선택된 정점에서 갈 수 있는 각 다음 정점들에 대해 

- 현재 알려진 최단거리
- 선택된 정점까지의 최단거리 + 선택된 정점에서 다음 정점까지의 거리

   중 가까운 거리로 최단거리를 갱신한다.

```python

```



```python
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

```


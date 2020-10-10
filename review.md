## 1194번. 달이 차오른다, 가자

- Point : 이동 횟수의 최솟값을 출력  -> BFS
- BFS의 핵심 -> visited 이 문제에서는 어떻게 적용할까..
- visited의 차원화 -> 상태가 바뀔때마다 새롭게 적용해 줘야 한다. 
- key가 6개이기 때문에 2^6개의 상태가 존재 가능함 -> visited는 2^6차원

```python
def bfs(x,y):
    queue = deque()
    # x,y, 주운 열쇠, 방문기록
    queue.append((x,y,0,0))
    visited[x][y][0] = 1
    while queue:
        # key = 갖고 있는 키의 상태
        # ex) key = 35 = 010011 -> 1,2,5번키 갖고있음 (bitmasking 개념)
        x,y,key,cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if iswall(nx,ny) and visited[nx][ny][key] == 0:
                # 목적지면 cnt return
                if matrix[nx][ny] == '1':
                    return cnt+1
                # 일반 위치면 key 상태 그대로
                elif matrix[nx][ny] == '.':
                    queue.append((nx,ny,key,cnt+1))
                    visited[nx][ny][key] = 1
                else:
                    # 소문자다 -> 열쇠다
                    if matrix[nx][ny].islower():
                        for i in range(len(keys)):
                            if matrix[nx][ny] == keys[i]:
                                # 키의 상태 변경
                                next_key = key | (1<<i)
                                queue.append((nx, ny, next_key, cnt + 1))
                                visited[nx][ny][next_key] = 1
                                break
                    # 대문자다 -> 문이다
                    else:
                        for i in range(len(doors)):
                            if matrix[nx][ny] == doors[i]:
                                # 키가 있는가 체크
                                if key & (1<<i):
                                    queue.append((nx,ny,key,cnt+1))
                                    visited[nx][ny][key] = 1
    return -1

doors = ['A','B','C','D','E','F']
keys = ['a','b','c','d','e','f']
# visited 가 2^6 차원인 이유? -> 가지고 있는 key의 상태마다 다르게 visited 체크해야함
visited = [[[0 for _ in range(1<<6)] for _ in range(M)] for _ in range(N)]
```

## 1261번. 알고스팟

- 전형적인 BFS 응용 문제
- visited에 벽 부순 횟수를 담고 그보다 작으면 빠꾸
- 보통은 BFS는 거리에 따라 방문순서가 정해짐 BUT 이 문제는 방문 순서대로 하면 안됨
- WHY? 벽 부순 기준대로 방문 체크해야함

```python
def solve():
    visited = [[float('inf') for _ in range(M)] for _ in range(N)]
    queue = deque()
    # x,y,벽 부순 횟수
    queue.append((0,0,0))
    visited[0][0] = 0
    while queue:
        x,y,cnt = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                # 벽 부순 횟수가 기존 보다 작으면 간다.
                if matrix[nx][ny] == 0 and visited[nx][ny] > cnt:
                    # 벽 안부섯으니까 cnt 그대로
                    queue.append((nx,ny,cnt))
                    visited[nx][ny] = cnt
                elif matrix[nx][ny] != 0 and visited[nx][ny] > cnt + 1:
                    # 벽 부섯으니까 cnt+1
                    queue.append((nx,ny,cnt+1))
                    visited[nx][ny] = cnt+1
    return visited[N-1][M-1]
```

## 1445. 일요일 아침의 데이트

- 다시 풀었음 생략

## 2146. 다리 만들기

- 분리 집합
- 분리 집합 문제 -> 다리가 이동하는 것이 아닌 육지가 이동
- 섬의 크기를 하나씩 늘리고 다른 섬과 처음 만날때, 그 섬의 증가된 크기의 합을 구함


# Algorithm 문제 풀 때, 고려해야 할 사항

- 배열을 앞으로 붙이는 건 말이 안됨

```python
# 나무 제테크 16235번
# 무언가 새로 들어오는 수가 1이고, 계속 늘어난다고 가정하자.
# 그렇다면 따로 정렬을 해줄 필요가 없다. 뒤나 앞에 넣어 주면 크기의 순서가 변경 되지 않기 때문
# 그럴때 새로운 수를 앞으로 넣는 방법과 뒤로 넣는 방법이 있는데,

list = [3,4,5] 
list = [0 for _ in range(leng)] + [3,4,5]

list = [5,4,3]
list = list + [0 for _ in range(leng)]

# 이 두개의 속도 차이는 어마어마 하므로 무조건 후자의 방법을 사용하자.
# why? 전자는 메모리 구조 전체를 바꿔야하기 때문이다.
```



- N X N 행렬을 탐색할 때, visited 는 N 이 작을 때는 1차원 배열으로 하고, N 이 클 때는 무조건 2차원 배열 방문으로 해야한다.

```python
# 1차원 visited, N > 100 일때 사용을 하지말자
visited = []
# 방문했을 시
visited.append((nx,ny))
# 방문 검사 
if (nx,ny) not in visited:

    
# 2차원 visited
visited = [[0 for _ in range(M)] for _ in range(N)]
# 꼭 2차원 일 필요 없음 각 상태를 저장하기 위해서는 3차원,4차원도 가능
# 시간에 따른 visited가 변경시 사용 가능 (ex 비트마스킹 문제)
```

- Deepcopy는 사용 자제하자.

```python
from copy import deepcopy

# 딥카피는 시간 초과를 고려했을 때 정말 왠만하면 사용 안 하는 것을 권장
# 하지만 언제써야하느냐? -> 그래프가 바뀔때는 사용해야함
# 즉 bfs시 그래프가 완전히 바뀌어 버려 각 queue마다 그래프를 저장하고 가야할때
# ex) 백준 청소년 상어 

# 그래프가 완전히 바뀌는 것이 아니라면 사용하지말고 visited를 사용하자.
# 각 경우마다 그래프가 바뀌는 것이 아닌 순서가 바뀌는 것이라면 그때마다 visited를 생성하여 체크하면 됨
# ex) 백준 연구소3
```

- 0718 백준 구슬 탈출 2

```python
# 백준 구슬 탈출 2
# 최대한 변수를 간단히 설정하고 가자.
# 어렵고 고려해야할 조건이 많아 까다로운 문제니까 다시 풀어보면 좋음

# 10번 이하로 움직여서 빨간 구슬을 구멍을 통해 빼낼 수 없으면 -1을 출력한다
r_x,r_y,b_x,b_y,cnt = queue.popleft()
if cnt > 10:
    return -1
# 이렇게 하면 틀림 why? 저렇게 하면 cnt가 10인 경우, 즉 그 r_x,r_y에 도달하기 위해 10번 움직인 것이므로 이미 실패
# 만일 저 상태에서 답을 찾으면 결과가 11로 나옴 

r_x,r_y,b_x,b_y,cnt = queue.popleft()
if cnt > 9:
    return -1
# 이렇게 해줘야 최대 결과 값이 10이 나옴
```

- 투 포인터 알고리즘 (reference: https://github.com/WooVictory/Ready-For-Tech-Interview/blob/master/Algorithm/%ED%88%AC%ED%8F%AC%EC%9D%B8%ED%84%B0%20%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98.md)

```python
# 시도했을 당시 틀렸던 포인트들:
# 1. 길이가 숫자가 1인 결과를 체크하지못하고 2로 출력하게 했음.
# 2. 1인 결과는 체크하나 마지막 숫자나 첫번째 숫자가 결과가 1인 최소값을 때를 골라내지 못함.
# 3. corner case에서 좀 더 디테일한 구현이 필요함.

start, end = 0, 0
sub_sum = matrix[0]
result = N+1
while True:
    if start == end:
        # result 가 1이 되어버리면 뒤에것 볼 필요 없음
        if sub_sum >= S:
            result = 1
            break
        # 둘 다 끝에 도달하면 break
        if end == N - 1 and start == N - 1:
            break
        # 아니라면 end를 한칸 앞으로 보내야 함
        else:
            end += 1
            sub_sum += matrix[end]
    # 부분합이 기준보다 크면 start를 앞으로 한칸 땡겨주고 부분합에서 전에 값 빼줌
    elif S <= sub_sum:
        result = min(result,end-start+1)
        sub_sum -= matrix[start]
        start += 1
    # 부분합이 기준보다 작다면 end를 앞으로 한칸 땡겨주고 부분합에서 나중 값 더해줌
    else:
        if end < N-1:
            end += 1
            sub_sum += matrix[end]
        # 만일 end가 N-1에 도착했지만 start는 도달 못했을 경우고 기준 값보다 작다?
        # start를 끝까지 땡겨줄 필요도 없이 끝내도 됨, 어차피 부분합은 작아지기만 하기때문
        else:
            break
```

- 0719 백준 미로탈출하기 

```python
# point 어차피 방향이 정해져있기 때문에 시작점 찾는 포인트를 한번만 돌아 줘도 상관 없음
# why? 그때 가면 돌아서 정해질 것이기 때문이다.
# 어지간한 bfs 문제는 visited를 이용하여 한번만 돌거나 방문했던 지점을 다시 방문하도록 하면 100% 시간초과 남.
# 어떠한 형태로던지 visited를 만들어 줘야함.
def search():
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                return (i,j)
    return (-1,-1)   
result = 0
while True:
    x,y = search()
    if (x,y) == (-1,-1):
        print(result)
        break
    else:
        result += bfs(x,y)    

# 미로를 탈출하지 못하는 경우는 두가지 경우
# 1. 돌다가 visited 체크된 경우를 만났을 때 (못가니까 뺑뺑 도는 경우)
# 2. 이미 못간다고 판명난 길을 가라고 할 때

# 미로를 탈출하는 경우
# 1. 진짜 밖으로 나감 (iswall = False)
# 2, 나갈 수 있다고 판명난 길을 가라고 할때

    elif visited[x][y] == 1:
        # 처음이면
        if flag:
            for i,j in step:
                visited[i][j] = -1
            return 0
        else:
            return cnt

 # 처음일때만 생각해줬는데 그건 아니고 전체의 경우에서 그렇게 해줘야함
# 즉 1인 경우를 만나더라도 내가 걸어온 길에 포함되면 탈출 못하는 거임
# 그 중복되는 경우를 해결하는 좋은 방법을 다음에 풀때는 생각해보자.
# 지금은 step으로 해결했음
```

- 7/23 백준 개리멘더링 2

```python
# 시간복잡도??
# N < 50 이라면 어지간하면 시간복잡도는 생각 안해도 되는 경우
# 이 문제에서 N<20이므로 시간복잡도 구해보자
# 기준점을 모든 점으로 한번씩 해줘야 함. -> 2중 for 문 N * N
# 그 안에서 d1,d2를 바꿔야 함. 
# 처음 접근 d1,d2 완전탐색 -> 시간복잡도 N * N
    for d1 in range(1,N):
        for d2 in range(1,N):
# 그러나 어차피 d1 + d2 < N 이므로 아래가 좀 더 최적화
    for d1 in range(1,N):
        for d2 in range(1,N-d1+1):

# 5가 되는 위치를 먼저 정해 준 뒤, 나머지 것을 채우는 식으로 했음
# 5가 되는 위치는 대칭이 아니므로 case를 나눠서 하드코딩 해줘야 함.
# 펜을 써서 빠르게 계산하는게 좋아보임
temp = r-x
if temp > d1:
    left = y -d1 + temp - d1
else:
    left = y - temp
if temp > d2:
    right =  y + d2 - (temp -d2)
else:
    right = y +temp

# 각 시작점, d1,d2 안에서 r,c를 각각 계산해줘야 함 시간 복잡도 * N * N
# 따라서 총 시간 복잡도 O(n) = N ^ 6 = 20 ^ 6 = 6400만 약 0.64초 이므로 OK
# 무식한 방법이지만 시간 복잡도를 좀 더 디테일 하게 계산하고 설계하자

```

- 0728 백준 드래곤커브

```python
# 기준점 만드는거 좀 잘한듯?
# critical point -> 지금 시작점이 변경돼서 간 곳이 제일 먼곳이고, 기준점이 된다.
x_cri,y_cri = step[-1]
length = len(step)-1
for st in range(length,-1,-1):
    # 90도 회전의 의미 -> 원점이 시작점으로 바뀐다고 생각하자.
	# x,y는 90도 회전 시킬 좌표 x_cri,y_cri는 기준점
	# x_var, y_var은 각 좌표가 원점에 있을때로 치환한 좌표
	# 시계 방향으로 90도 회전 -> x에 좌표에 y변화량 더하고 y좌표에 x좌표 뺀다.(일정)
    x,y = step[st]
    x_var,y_var = x - x_cri, y - y_cri
    nx,ny = x_cri+y_var , y_cri-x_var
    if iswall(nx,ny):
        matrix[nx][ny] = 1
        step.append([nx,ny])
```

- 0731 백준 새로운 게임2

```python
# 빡구현 문제
# 오랜만에 풀어서 그런가 체계적으로 접근하지 못함
# 함수화 해서 푸는게 좋은 것 같음 + 문제 설계를 착실히 해야함

# 함수화 에서는 각각의 경우를 나눠서 풀자
# 처음에 짠 코드는 엉망이 었다 -> 복잡하더라도 중복된 코드를 최소화 하여 풀어야함

# 생각 -> 하얀색이나 빨간색은 거의 똑같으나 차이는 마지막에 뒤집어 주는 것 
# moving 을 함수화 하여 중복 최소화

def moving(nx,ny,x,y,idx):
    # state에서 움직이는데, 움직이는 함수를 어떻게 구현할까?
    # 하나하나 움직이지말고 단체로 움직이면 됨. 
    # 어차피 본인보다 위에 있는 애들은 세트로 움직임
    stack = []
    for i in range(len(state[x][y])-1,-1,-1):
        temp = state[x][y].pop()
        stack.append(temp)
        data[temp][0],data[temp][1] = nx,ny
        if temp == idx:
            break
    return stack

def go_white(nx,ny,x,y,idx):
    state[nx][ny] += moving(nx,ny,x,y,idx)[::-1]

def go_red(nx,ny,x,y,idx):
    state[nx][ny] += moving(nx,ny,x,y,idx)
 
# 파란색이나 벽이나 경우가 똑같으므로 중복 코드 최소화
# 이 경우 방향 바꿔주고 한번 더해야함 -> 빨간색 하얀색을 함수화 하므로써 중복 최소화.
# 튕겼을 때 또 튕긴다? -> 방향만 바꿔줌 , 빨간색or하얀색이다? -> 똑같이 처리하고 방향바꿈
if iswall(nx,ny) == False or matrix[nx][ny] == 2:
    if d == 1: d = 2
    elif d == 2: d = 1
    elif d == 3 : d = 4
    elif d == 4 : d = 3
    nx,ny = x+dx[d],y+dy[d]
    if iswall(nx, ny) == False or matrix[nx][ny] == 2:
        data[iteration][2] = d
        nx,ny = x,y
        elif matrix[nx][ny] == 0:
            go_white(nx,ny,x,y,iteration)
            data[iteration][2] = d
        elif matrix[nx][ny] == 1:
            go_red(nx,ny,x,y,iteration)
            data[iteration][2] = d
```

- 0804 백준 파티

```python
# 맨 처음 나의 생각 => 다익스트라 알고리즘으로 (start,end)간의 거리를 전부 구해준다.
# distance 구해 놓은 것들을 버려야 하므로 so bad
def search(start_point, end_point):
	# ... #
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

# 더 좋은 idea => 시작점을 end_point로 하면 배열 distance[i]의 의미는?
# 도착점에서 i 로 갈때 걸리는 거리.. 즉 올 때의 거리
# graph를 뒤집어서 저장하면? distance[i]는 i에서 end_point로 가는 거리.
def search(start_point, graph):
    # ...
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

# path는 start에서 end로 갈때의 비용, reverse는 end에서 start 로 갈때의 비용
for _ in range(M):
    start, end, cost = map(int,input().split())
    path[start].append((end,cost))
    reverse[end].append((start,cost))
    
dis = search(end_point,path)
rev_dis = search(end_point,reverse)
```

- 0805 벽 부수고 이동하기 2

```python
# 처음 접근
# 잘못된 점 1. bfs는 cnt가 커지는 순서로 queue에 담긴다. => visited[nx][ny][k] < cnt 는 당연하다.
# 잘못된 점 2. visited에 거리 체크를 동시에 하면 queue에 cnt를 담을 필요가 없으므로 메모리를 아낄 수 있다.
visited = [[[-1 for _ in range(K+1)] for _ in range(M)] for _ in range(N)]
def bfs(x_start,y_start,x_end,y_end):
    queue = deque()
    # x위치, y위치, 거리, 벽뚫은 횟수
    queue.append((x_start,y_start,1,0))
    visited[x_start][y_start][0] = 1
    while queue:
        x,y,cnt,k = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                # bfs는 어차피 cnt 순서이므로 항상 visited[nx][ny][k] < cnt 이다.
                if visited[nx][ny][k] == -1 or visited[nx][ny][k] > cnt:
                    if nx == x_end and ny == y_end:
                        return cnt+1
                    if matrix[nx][ny] == 1 and k < K:
                        queue.append((nx,ny,cnt+1,k+1))
                        visited[nx][ny][k+1] = cnt+1
                    elif matrix[nx][ny] == 0:
                        queue.append((nx,ny,cnt+1,k))
                        visited[nx][ny][k] = cnt+1
# 수정된 코드 => 메모리 초과는 안나지만 아슬아슬함. visited 구조가 비 효율적이다.                    
def bfs(x_start,y_start,x_end,y_end):
    if x_end == 0 and y_end == 0:
        return 1
    queue = deque()
    # x위치, y위치, 벽뚫은 횟수
    queue.append((x_start,y_start,0))
    visited[x_start][y_start][0] = 1
    while queue:
        x,y,k = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                if visited[nx][ny][k] == -1:
                    if nx == x_end and ny == y_end:
                        return visited[x][y][k]+1
                    if matrix[nx][ny] == 1 and k < K:
                        queue.append((nx,ny,k+1))
                        # visited에 바로 거리 체크
                        visited[nx][ny][k+1] = visited[x][y][k]+1
                    elif matrix[nx][ny] == 0:
                        queue.append((nx,ny,k))
                        visited[nx][ny][k] = visited[x][y][k]+1
                        
# 비트 마스킹을 활용하면 N X M X K 만큼의 visited 메모리를 N X M 만큼만 사용하면 된다.
# 비트 마스킹 활용? => 각 상태별 visited 체크만 할 때, 즉 상태별 최단 거리를 구할 때.
# K 만큼 벽 뚫은 것 visited 검사
if visited[nx][ny] & (1<<k):
# K 만큼 벽 뚫은 것 visited 입력
visited[nx][ny] = visited[nx][ny] | (1<<k)
```

- 0805 군대 탈출 (good)

```python
# 구현 아이디어 : visited로 통과 했을 때의 최소값과 통과 하지 않았을 때의 최소값 구하기
# 벽 부수고 이동하기 2와 다른점은? => 벽 부수고 이동하기 2는 구하고자 하는 값이 거리
# 어차피 거리기 때문에 처음 만나는 값이 곧 최소값
# 하지만 군대 탈출은 거리가 아닌 다른 value 이므로 체크만 하는 것이 아닌 최소값 저장하고
# 그보다 작은 값만 체크해야함

# 틀린 점 : 
visited = [[[987654321,987654321] for _ in range(M)] for _ in range(N)]
# 각 값 k 가 0 <= k <= 10^9 이었는데, 987654321 보다 10^9 이 커서 정답이 안나오는 경우가 있었음. 값을 체크 하거나 아예 float('INF')로 해도 좋음
visited = [[[9876543210,9876543210] for _ in range(M)] for _ in range(N)]

# 핵심 로직
while queue:
    # x 위치, y 위치, 지나온 경로 중 최대값, 통과 여부
    x,y,val,k = queue.popleft()
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if iswall(nx,ny):
            # 이때까지의 최대값과 새로 간 곳의 값 비교해서 최대값 갱신
            temp = max(val,matrix[nx][ny])
            # 그 최대값이 이전에 방문했던 경로의 최대값보다 크면 cut
            if visited[nx][ny][k] > temp:
                queue.append((nx,ny,temp,k))
                visited[nx][ny][k] = temp
            # 통과 해보지 못했으면 왔던 방향으로 통과해보고 과거의 값보다 크면 cut
            # 처음에는 visited[nx][ny][k] > temp 여야만 이 분기를 검사했는데,
            # 그러면 틀림 why? visited[nx][ny][k] > temp를 성립하지 않아도 건너뛰어서 최소값이 될수 있기 때문
            if k == 0:
                nnx,nny = nx+dx[i],ny+dy[i]
                if iswall(nnx,nny):
                    temp = max(val,matrix[nnx][nny])
                    if visited[nnx][nny][1] > temp:                            				                                         queue.append((nnx,nny,temp,1))
                        visited[nnx][nny][1] = temp
```

- 0807 불!

```python
# 틀린 요소

# 1. 당연히 불은 하나라고 생각했다. 불이 여러개 일 수 있고 하나일 수도 있다.
# 2. 가장자리라고 해서 당연히 x,y 가 N-1, M-1 일 경우를 생각했는데 0일 경우도 있었다.
# 3. 불을 옮기고 나면 원래 있던 불은 QUEUE에서 나가야하는데 그냥 FOR문 돌려서 메모리 초	과가 났었다.
# 4. 불 먼저 옮기고 사람 옮기는데, cnt가 바뀌면 불을 옮겨야 한다. 그럼 처음 시작할 때 cnt = 0 일 때부터 불을 옮겨야 함.
```

- 0808 낚시왕

```python
# 처음 구현 했을 때 시간이 많이 걸린 이유?
# 추측 => 행렬을 계속 복사해서 그럴것이다.
    new = [[[0,0,0] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if matrix[i][j][2] != 0:
                s,d,z = matrix[i][j]
                sharkmoving(i,j,s,d,z)
    matrix = new
    
# 행렬 복사 없이 하는 아이디어 구상 => 기존 matrix 행렬을 변형
# 행렬 복사하는 이유는 움직인 물고기와 움직여야 할 물고기를 구분하기 위함.
# matrix를 2개로 쪼개서 col이 짝수 일때는 짝수 출발 홀수 도착, 그 반대는 반대로 함
# 하지만 별 시간 차이 없음
matrix = [[[[0,0,0],[0,0,0]] for _ in range(C)] for _ in range(R)]
for col in range(C):
    result = fishing(col,result,col)
    for i in range(R):
        for j in range(C):
            if matrix[i][j][col%2][2] != 0:
                s,d,z = matrix[i][j][col%2]
                sharkmoving(i,j,s,d,z,col)
# 원인: 벽에 맞는 것 체크하기 위해 s만큼 for문 돌려 일일히 체크 해줌 -> 시간 걸림
# for문의 횟수를 줄여야함
def sharkmoving(x,y,s,d,z,col):
    matrix[x][y][col%2] = [0,0,0]
    for i in range(s):
        nx,ny = x + dx[d], y+dy[d]
        if not iswall(nx,ny):
            if d== 1: d=2
            elif d==2: d=1
            elif d==3: d=4
            elif d==4: d=3
            nx,ny = x + dx[d],y + dy[d]
        x,y = nx,ny
    if matrix[x][y][(col+1)%2][2] < z:
        matrix[x][y][(col+1)%2][0],matrix[x][y][(col+1)%2][1],matrix[x]

# s만큼 돌지 말고 수식적으로 계산해야 함
def sharkmoving(x,y,s,d,z):
    matrix[x][y] = [0,0,0]
    s_start = s
    while True:
        nx,ny = x + s * dx[d], y+ s * dy[d]
        if nx < 0:
            s = s-x
            x, d = 0,2
        elif nx >= R:
            s = s-(R-1-x)
            x, d = R-1,1
        elif ny < 0:
            s = s -y
            y, d = 0,3
        elif ny >= C:
            s = s-(C-1-y)
            y, d = C-1,4
        else:
            break
    if new[nx][ny][2] < z:
        # s_start의 의미? => 방향은 벽에 부딪히면 바뀌지만 s는 처음 값이 들어가야함
        new[nx][ny][0],new[nx][ny][1],new[nx][ny][2] = s_start,d,z
```

- 0809 백준 컵라면

```python
# greedy 알고리즘 -> 필요한 것만 계산하면 된다. 필요한 것과 없는 것을 구분하자.
# 대부분은 시작 부터 끝 까지 계산하는 것이 아닌, 끝에서 시작점을 찾아가는 경로를 구한다.
# 시작점부터 하나하나 계산하면 100% 시간초과. 필요한 것만 수식적으로 계산해야함.

# 이 문제에서 필요한 것? -> 최대 컵라면 수 만 알면 된다.
# 필요없는 것? -> 몇 번째 순서에 뭐를 풀었는지는 중요하지 않다!

# 설계 -> 각 데드라인 까지의 해야 하는 일을 모은다.
data = [[] for _ in range(N+1)]
for i in range(N):
    a,b = map(int,input().split())
    data[a].append(b)
# 그 다음 각 데드라인 별로 컵라면 갯수에 따라 정렬한다.
for i in range(N):
    if len(data[i]):
        data[i].sort(reverse=True)
# 각 데드라인 별로 가장 큰 것을 저장하고 그 다음 숫자부터 지금 값의 최소값을 넣는다.
# 만일 데드라인 까지 해야 하는 일이 없다면 뒤에 나올 데드라인 중 가장 큰 값을 넣기 위해 0을 넣는다.
heap = []
heapq.heapify(heap)
for i in range(1,N+1):
    if len(data[i]) != 0:
        # 제일 큰 거 추가하고
        heapq.heappush(heap,data[i][0])
        # 그다음꺼 부터 도는데, 지금 있는 것 중에 가장 작은 거 보다 다음께
        for j in range(1,len(data[i])):
            temp = heapq.heappop(heap)
            # 크다? 그럼 다시 넣고 끝
            if temp > data[i][j]:
                heapq.heappush(heap,temp)
                break
            # 아니다? 그럼 데이터를 넣고 다시
            else:
                heapq.heappush(heap,data[i][j])
    else:
        heapq.heappush(heap,0)
        
# 가장 greedy 같이 푼 코드

pq = []
result = 0
# greedy 답게 데드라인의 역순부터 시작한다.
# 쉽게 생각하면 데드라인 역순부터 돌면서 모든 후보를 집어 넣는다 
# -> 역순부터 하기 때문에 못하는 건 들어가 있지 않다.
# -> 이 데드라인때 할 수 있는 모든 일의 요소 이다. 그중 최대값 뽑아서 result에 더함
for i in range(max_dead, 0, -1):
    
    for j in dead_list[i]:
        heapq.heappush(pq, -j)
    if pq:
        result -= heapq.heappop(pq)

```

- 0809 백준 계산기 (다시 풀어보자)

```python
# 역시 greedy 문제
# 1. 구할 것을 정확하게 파악한다. 
# -> 연산 순서.
# 2. 역순부터 시작한다.
# -> 0부터 하면 헷갈린다. N 부터 숫자를 줄여나가야 한다.
# 3. 필요한 것만 수식적으로 계산해야 한다.(for문으로 탐색형식하면 터짐)
# -> 모든 경우의 수를 직접 돌리면 시간초과 난다. 필요한 연산만 해서 가짓수를 줄여야한다.

N = int(input())
result = []
# 100000 꼴로 만들어 줘야 함.
while True:
    # N & 1 = 1 : 끝자리가 1이다 -> 홀수다 못만들기 때문에 *2
    if N & 1:
        result += ['[/]']
        N = N * 2
    # N & 2 = 1: 뒤에서 두번째 자리가 1이다 -> 없애 준다.
    elif N & 2:
        result += ['[+]']
        N = N -2
    # N = N //2 를 이진수 측면에서 보면 맨 뒷자리를 없애준다.
    # 하지만 N이 짝수 일때만 만족하는 경우다.
    else:
        result = result + ['[*]']
        N = N //2
    if N == 0:
        break

print(len(result))
print(*result[::-1])
```

- 0812 백준 키 vs 달이 차오른다 가자

```python
#  두 문제의 차이점이 뭘까?
# 키 -> 주운 문서의 갯수    달이 차오른다 가자 -> 최단거리
# 최단거리는 비트마스킹이 필요하고, 그게 아니면 꼭 쓸필요없다.(갈수 있는지 없는지만 알자)
# 경로가 중요하다 -> 비트마스킹으로 열쇠 주울때 마다 초기화
# 경로 필요없고 갈수 있냐 없냐만 중요 -> visited 1차원으로 한번만 돌자

# 달이 차오른다 가자 -> 최단거리 이므로 열쇠 주울 때 마다 visited 초기화 해서 
# 움직이는거 체크 해줘야 함
# visited[x][y] | (1<<cnt) 방문시 체크 : cnt -> 주운 열쇠 갯수
# cnt가 증가 할수록 밀리는 갯수가 늘어 visited가 초기화 하는 효과
# 키는 6개 -> 0~31로 각각의 키 보유 상황을 체크 가능하다.
# ex) key = 27 => 011011 (1,2,4,5번 열쇠를 보유하고 있다.)
# ex) if visited[x][y] == 27 하면 (1,2,4,5번 열쇠를 보유한 상태일때 방문했는가?)

# 키 -> 최단 거리가 아니기 때문에 visited를 초기화 해줄 필요 없다.
# visited를 초기화 할 필요 없다? -> 그냥 열쇠 주우면 돌아가면 됨, 
# 문에 막혀 못가는 곳 있으면 가고 아니면 말고
# 최단거리 구하는게 아니기 때문에 비트마스킹 할 필요없다.
# 로직 
# 1. 입구를 하나씩 순서상관없이 입장
# 2. 문에 갔는데 열쇠가 없어서 못여네? -> 딕서너리에 키와 좌표 저장
# 3. 지나가다가 열쇠를 찾았네? -> 그 딕서너리로 가서 그 키의 좌표들 queue에 append
# 문 입장 순서는 상관없는 이유 -> 못여는 문은 위치 담아두고 나중가서 열쇠 찾으면 가면 되고
# 갔는데 열쇠가 있으면 그냥 열면 되고 끝까지 못주우면 못가는 위치인거고.
# visited는 비트마스킹 필요없는 이유 -> 어차피 갈수있나 없나만 보는건데 뭐. 경로가 중요한게 아니잖아.
```

- 0816 컬러볼

```python
# idea -> brute force( 완전 탐색 )
# 공하나씩 돌면서 자기보다 큰 경우를 전부 센다.
# 시간 복잡도 O(n^2) 이므로 불가능 -> log(n) 이나 nlog(n)의 방법을 찾아야 한다.

# 첫번째 idea -> 정렬 후 숫자가 낮은 것 부터 본다.
# 낮은 것부터 보면서 그때까지의 전체 합을 구하고 본인의 색깔을 뺀다.
# 유의할 점 -> 크기가 같은 공들을 처리해 줘야함
N = int(input())
data = []
for i in range(N):
    color,size = map(int,input().split())
    data.append([size,color,i])
result = [0 for _ in range(N)]
# 색깔 별 크기 합 저장
color_sum = [0 for _ in range(N+1)]
# 볼의 크기를 기준으로 정렬
data.sort()
total_sum, now = 0, 0
for size,color,idx in data:
   	# 같은 크기의 볼들을 처리하기 위한 알고리즘
    if now == size:
        # temp를 dictionary로 정의하는 이유? 
        # dictionary 의 in 함수는 시간복잡도 O(1) 이다.
        if color in temp:
            result[idx] = val - temp[color]
        else:
            result[idx] = val - color_sum[color]
            temp[color] = color_sum[color]
    # 같지 않고 다음으로 넘어가면 바뀜
    else:
        # 인덱스의 값은 이때까지 지나온 모든 공의 크기 합 - 내가 속한 볼의 크기 합
        temp = {color:color_sum[color]}
        result[idx] = total_sum - color_sum[color]
        now, val = size, total_sum
    color_sum[color] += size
    total_sum += size

for num in result:
    print(num)
       
# 더 좋은 idea -> 굳이 sort를 해야하나?
# 공의 최대 값이 정해져 있다 -> 입력 받을 때 부터 정해진 위치에 넣으면 알아서 정렬됨

N = int(input())
# 공의 크기 순으로 모아둠
data = [[] for _ in range(2001)]
for i in range(N):
    color,size = map(int,input().split())
    data[size].append((color,i))
result = [0 for _ in range(N)]
color_sum = [0 for _ in range(N+1)]
total_sum = 0
for size,arr in enumerate(data):
    temp,temp_size = {},0
    # 각 크기마다 공을 꺼냄 (자동으로 크기 순으로 꺼내짐)
    for color,idx in arr:
        if color in temp:
            result[idx] = total_sum - temp[color]
        else:
            result[idx] = total_sum - color_sum[color]
            temp[color] = color_sum[color]
        color_sum[color] += size
        temp_size += size
    total_sum += temp_size

for num in result:
    print(num)
```

- 0820 색종이 붙이기

```python
# 처음 접근 -> 그냥 순서대로 지우기.
# 경우의 수를 따질 수 없다. 최적의 해도 존재 하지 않으므로 Brute Force
# 어떨때 Brute Force? -> 무엇이 최적의 해 인지 끝까지 해봐야 아는 경우.
# 예를 들면 지금 최선의 경우를 골랐다 하더라고 마지막 까지 갔을 때 그것이 최선이라는
# 보장이 없다. 그 순간 최적을 고르면 -> Greedy Algorithm

# 문제 푸는 방법 -> 하나씩 해봐야 한다. (재귀로)
def solve(matrix,frequency):
    if sum(frequency) >= result[0]:
        return
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 1:
                # 크기가 5인 것 부터 체크해서 되면 출발
                # dfs의 원리, 맨 처음 5부터 출발해서 끝까지 가보고 아니면 돌아옴
                # 만일 처음이 5가 아니라면 그 뒤도 전부 아니므로 가지치기
                for k in range(5,0,-1):
                if i < 11-k and j < 11-k and frequency[k] < 5:
                        if Check(i, j, 5 ,matrix):
                            Make(i, j, 5, matrix)
                            frequency[5] += 1
                            solve(deepcopy(matrix),frequency[:])
                            frequency[5] -= 1
                            Reverse(i, j, 5, matrix)
                # 경우의 수 다 해보고 이 가지는 return
                # 만일 위의 for문에서 걸렸다면 다음 가지로 갔을 것이고
                # 못갔다면 더 이상 유망하지 못한 가지.
                return
    result[0] = min(result[0],sum(frequency))
    
    
# 처음 접근 시 시간 초과 이유.
# 1. 현재 result 보다 현 상태가 크면 return (가지치기) 해야 함.
if sum(frequency) >= result[0]:
    return

# 2. deepcopy가 필요없음
if i < 11-k and j < 11-k and frequency[k] < 5:
    if Check(i, j, 5 ,matrix):
        Make(i, j, 5, matrix)
        frequency[5] += 1
        # 어차피 그 당시의 matrix상태로 끝까지 가기 때문에 deepcopy를 해서 
        # 넘겨줄 필요가 없음
        # 재귀로 permutation 만드는 원리를 상기 시켜보기 바람.
        solve()
        frequency[5] -= 1
        Reverse(i, j, 5, matrix)
```

- 0822 일요일 아침의 데이트

```python
# 생각은 빠르게 했으나 구현 과정에서 디테일이 부족해서 시간을 낭비함
def bfs(x,y):
    queue = deque()
    queue.append((x,y,[0,0]))
    visited[x][y] = [0,0]
    while queue:
        x, y, step = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                temp = step[:]
                # 이전의 조건으로 먼저 검사하고 그 뒤의 temp 변경 -> 일관적으로 검사되지 못함
                # 왜? 이전에는 조건에 맞았는데 바뀌고 나면 조건에 안맞으고 실질적으로 들어가는 것은 조건에 안맞는 것들
                # 따라서 변경된 값으로 조건 검사를 하고 맞으면 추가 이런식으로 해야함
                if visited[nx][ny][0] > step[0] or (visited[nx][ny][0] == step[0] and visited[nx][ny][1] > step[1]):
                    if matrix[nx][ny] == 'F':
                        visited[nx][ny] = temp
                        continue
                    elif matrix[nx][ny] == 'a':
                        temp[1] += 1
                    elif matrix[nx][ny] == 'g':
                        temp[0] += 1
                    queue.append((nx, ny, temp))
                    visited[nx][ny] = temp
                    
# 무엇이 틀렸을까? -> 'a'를 지나는 경우와 'g'를 지나는 경우, 일반을 지나는 경우 모두 visited가 갱신되는 조건이 다르다
# if visited[nx][ny][0] > step[0] or (visited[nx][ny][0] == step[0] and visited[nx][ny][1] > step[1]):
# 이렇게 통일된 조건을 검사하고 통과하면 temp가 +1 이런식으로 되는데, 그렇게 되면 제대로 visited가 체크되지 않는다

def bfs(x,y):
    queue = deque()
    queue.append((x,y,[0,0]))
    visited[x][y] = [0,0]
    while queue:
        x, y, step = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                temp = step[:]
                if matrix[nx][ny] == 'F':
                    if visited[nx][ny][0] > step[0] or (visited[nx][ny][0] == step[0] and visited[nx][ny][1] > step[1]):
                        visited[nx][ny] = temp
                        continue
                # 조건에 의해 먼저 변경하고
                elif matrix[nx][ny] == 'a':
                        temp[1] += 1
                elif matrix[nx][ny] == 'g':
                        temp[0] += 1
                # 그 변경된 값으로 조건 검사 해서 맞으면 추가
                if visited[nx][ny][0] > temp[0] or (visited[nx][ny][0] == temp[0] and visited[nx][ny][1] > temp[1]):
                    queue.append((nx, ny, temp))
                    visited[nx][ny] = temp
                    
# 항상 조건 검사할때 변경사항이 있다면 변경 -> 조건 검사 후 vistited 와 queue/stack 변경 이순서!!!
# 즉 다시말해 변경된 조건으로 체크를 해야 한다면, 먼저 변경을 해본 후 조건 검사 해야 한다.
```



- 0823 피리부는 사나이

```python
# 처음 접근 -> 그냥 하나씩 돌아서 되는 자기들 끼리 도는 것 만큼 숫자 올려줌 (오답)
# 왜냐? 출발점에서 안 이어지지만 뒤에서 이어지는 경우가 있음
def bfs(x,y,cnt):
    queue = deque()
    queue.append((x,y,[[x,y]]))
    visited[x][y] = cnt
    while queue:
        x,y,step = queue.popleft()
        dx,dy = direction[matrix[x][y]]
        nx,ny = x+dx, y+dy
        # 안들린 점이 있으면 내걸로 만들고
        if visited[nx][ny] == 0:
            queue.append((nx,ny,step+[[nx,ny]]))
            visited[nx][ny] = cnt
        # 내 점이랑 이어지네? -> circular 하다는 거니까 내 영토
        elif visited[nx][ny] == visited[x][y]:
            result[0] += 1
            return cnt+1
        # 다른 점이랑 만났네? -> 나는 그 영토에 소속이었네
        elif visited[nx][ny] != visited[x][y]:
            temp = visited[nx][ny]
            for x1,y1 in step:
                visited[x1][y1] = temp
            return cnt+1

    return cnt+1

# 더 좋은 방법을 생각해야 한다. -> step으로 꼭 visited를 일일히 바꿔줄 필요가 있을까?
# 정확한 visited가 연결되는 것을 원하는게 아니라 몇개가 연결되어 있는지만 알면 되는데?
# cnt가 점점 커지는 구조이므로 visited[nx][ny] < visited[x][y] 이면 다른 graph와 만나는 것임을 알수 있다.
# 따라서 visited를 정확하게 맞춰주지 않아도 경로의 갯수를 구할 수 있음

def bfs(x,y,cnt):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = cnt
    while queue:
        x,y = queue.popleft()
        dx,dy = direction[matrix[x][y]]
        nx,ny = x+dx, y+dy
        # 안들린 점이 있으면 내걸로 만들고
        if visited[nx][ny] == 0:
            queue.append((nx,ny))
            visited[nx][ny] = cnt
        # 내 점이랑 이어지네? -> circular 하다는 거니까 내 영토
        elif visited[nx][ny] == visited[x][y]:
            result[0] += 1
            return cnt+1
        # 다른 점이랑 만났네? -> 나는 그 영토에 소속이었네
        elif visited[nx][ny] < visited[x][y]:
            return cnt+1

    return cnt+1

```

- 0827 프로그래머스 단어 변환

```python
# 모든 테스트 케이스가 잘 안된다? -> 무조건 끝쪽을 생각해야 한다.
# 안될때 반드시 체크 해야 할 점.
# 1. 0일때 잘 나오느냐
# 2. 0을 제외한 첫 번째 수가 잘 나오느냐
# 3. 마지막 케이스가 잘 들어가느냐

# 대부분의 케이스는 queue에 담을때와 나올때가 문제다.
# while queue 하기 위해 처음에 queue를 담는데, 그때 끝나버릴수도 있다.
# 그래서 queue에 담을 때도 체크를 해줘야 한다.
# 그리고 보통 queue 안에서 return 할때가 아닌 끝나고 결과 보고 return 하는 경우가
# 있는데 그때도 한번 더 체크해주고 return 해야 한다.
from _collections import deque

def solution(begin, target, words):
    queue = deque()
    for word in words:
        if isword(begin,word):
            # 이걸 고려안해서 틀림
            # while queue 돌기 전에 끝나는 경우 ( 0을 제외한 첫 번째 수)
            # 이걸 항상 고려해 줘야 한다.
            if word == target:
                return 1
            else:
                queue.append((word,[word]))
    while queue:
        print(queue)
        now , step = queue.popleft()
        for word in words:
            if word not in step and isword(now,word):
                if word == target:
                    return len(step)+1
                else:
                    queue.append((word,step+[word]))
    return 0

def isword(now,word):
    cnt = 0
    for idx,alpha in enumerate(word):
        if alpha != now[idx]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False
```


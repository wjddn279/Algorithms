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


## Bitmasking

- 비트마스킹의 의미? 활용?

```python
# 3차원 배열 visited = 10 * M * N의 메모리 활용
visited_array = [[[0 for _ in range(10)] for _ in range(M)] for _ in range(N)]
# bitmasking M*N 만큼의 메모리 활용
visited_bit = [[0 for _ in range(M)] for _ in range(N)]

# 그냥 방문 체크
visited_array[x][y][i] = 1
# 비트마스킹 방문 체크 -> 2진수의 i번째 자리를 1로 만듬
visited_bit[x][y] = visited_bit[x][y] | (1<<i)

# 그냥 방문 확인
if visited_array[x][y][i]:
# 비트마스킹 방문 확인 -> 2진수로 바꾸었을때 i번째 자리가 1인가 확인
if visited_array[x][y] & (1<<i)

# 꼭 visited 체크일때만 쓰이는건 아님 1,0의 배열을 하나의 숫자로 나타내는 것도 가능함
# ex) 35 = 010011 / [0,1,0,0,1,1] 과 같은 의미로 사용이 가능하다.
```

## BFS/DFS 방향 회전

```python
# 동 북 서 남 -> +1 : 시계 방향(왼쪽) , -1 : 반 시계 방향(오른쪽)
dx = [0,-1,0,1]
dy = [1,0,-1,0]
# 현재 방향 d
# ld (왼쪽으로 회전한 방향)
ld = (d+1)%4
# rd (오른쪽으로 회전한 방향)
rd = (d+3)%4
```

## 막대기 회전시 돌아도 되는지 체크

```python
# d가 0이면 현재 가로 상태, d가 1이면 현재 세로 상태 
def turn(x,y,d):
    # i는 항상 x , j는 항상 y 임을 유의 하자.
    if d == 0:
        # range 범위 헷갈릴때? -> 그냥 for i in [x-1,x,x+1] 로 써주는 것도 직관적일듯
        for i in range(x-1,x+2):
            for j in range(y,y+3):
                if not iswall(i,j):
                    return -1,-1,False,0
        return x-1,y+1,True,1
    else:
        for i in range(x,x+3):
            for j in range(y-1,y+2):
                if not iswall(i,j):
                    return -1,-1,False,0
        return x+1,y-1,True,0
```

## 조합, 순열, 부분집합

```python
def combination(n,k,r,step):
    if k == r:
        print(step)
        return
    if k >= n:
        return
    combination(n,k+1,r,step+[arr[k]])
    combination(n,k+1,r,step)
    
def permutation(n,k,r):
    if k == r:
        print(a)
        return
    for i in range(k,n+1):
        a[i],a[k] = a[k],a[i]
        permutation(n,k+1,r)
        a[i],a[k] = a[k],a[i]
        
def powerset(n,k,step):
    if n == k:
        print(step)
        return
    powerset(n,k+1,step+[arr[k]])
    powerset(n,k+1,step)
```

## 깨진 블록들 밑으로 정렬

```python
# M : 너비, N : 높이 , now : 현재 지도
# 오른쪽으로 한칸씩 가면서
for j in range(M):
    # 밑부터 차례대로 
    for i in range(N-2,-1,-1):
        for l in range(i,N-1):
            # 현재 위치에서 한칸 밑과 비교해서 나는 블록이 있고 밑에는 없다면 교체
            if now[l][j] and not now[l+1][j]:
                now[l][j],now[l+1][j] = now[l+1][j],now[l][j]
            # 아니면 그만
            else:
                break
```

## 배열 회전 관련 skill

```python
# 90도 회전 -> 기본적으로 x,y 대칭 
def rotate():
    new_matrix = [[0] * len(matrix) for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix[j][len(matrix)-i-1] = matrix[i][j]
    return new_matrix

# 후        전
# 1 1 1 1   1 2 3 4
# 2 2 2 2   1 2 3 4 
# 3 3 3 3   1 2 3 4
# 4 4 4 4   1 2 3 4 

# 180도 회전
def rotate():
    new_matrix = [[0] * len(matrix) for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix[len(matrix)-i-1][len(matrix)-j-1] = matrix[i][j]
    return new_matrix

# 270도 회전
def rotate():
    new_matrix = [[0] * len(matrix) for i in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new_matrix[len(matrix)-j-1][i] = matrix[i][j]
    return new_matrix
```

## 한칸씩 회전

```python
def rotate(x,y,R):
    # x,y : 중심 R : 회전 반경
    for r in range(1,R+1):
        temp = matrix[x-r][y-r]
        # 위쪽
        for j in range(y-r,y+r):
            new = matrix[x-r][j+1]
            matrix[x-r][j+1] = temp
            temp = new
        # 오른쪽
        for i in range(x-r,x+r):
            new = matrix[i+1][y+r]
            matrix[i+1][y+r] = temp
            temp = new
        # 아래쪽
        for j in range(y+r,y-r,-1):
            new = matrix[x+r][j-1]
            matrix[x+r][j-1] = temp
            temp = new
        # 밑쪽
        for i in range(x+r,x-r,-1):
            new = matrix[i-1][y-r]
            matrix[i-1][y-r] = temp
            temp = new
```

## 2차원 배열 복사

```python
matrix = [[0 for _ in range(M)] for _ in range(N)]
5
# deepcopy 보다 빠름
copy = [i[:] for i in matrix]
```


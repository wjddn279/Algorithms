# 10시 40분
import sys
sys.stdin = open("new_game2_17839.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()
# 체스판의 크기 N , 말의 개수 K
# 0 : 흰  1 : 빨  2  : 파
# 우,좌,상,하
def iswall(x,y):
    if x < 0 or y < 0 :
        return False
    elif x >= N or y >= N:
        return False
    else:
        return True

global N,K
N, K = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
data = []
for i in range(K):
    x,y,d = map(int,input().split())
    data.append([x-1,y-1,d])
state = [[[] for _ in range(0,N)] for _ in range(0,N)]
for idx,da in enumerate(data):
    x,y,d = da
    state[x][y].append((idx,d))

dx = [0,0, 0, -1, 1]
dy = [0,1, -1, 0, 0]
# 말이 이동하려는 칸이 흰색 :
# 다 같이 그 칸으로 이동하고 이미 말이 있다면 가장 위에 그 말을 올려 놓음
# A,B,C 가 D, E 위로 이동 -> D,E,A,B,C
print(data)
prin(state)
new_state = [[[] for _ in range(N)] for _ in range(N)]
for x, y, d in data:

    nx, ny = x + dx[d], y + dy[d]
    if iswall(nx, ny):
        print(nx,ny)
        if matrix[nx][ny] == 0:
            new_state[nx][ny] += state[x][y]
        elif matrix[nx][ny] == 1:
            new_state[nx][ny] += state[x][y][::-1]
        elif matrix[nx][ny] == 2:
            if d == 1: d = 2
            elif d == 2: d = 1
            elif d == 3: d = 4
            else: d = 3
            nx,ny = x + dx[d], y + dy[d]
            if not iswall(nx,ny) or matrix[nx][ny] == 2:
                pass
            else:
                new_state[nx][ny] += state[x][y]
    prin(new_state)

# 빨간색:
# 이동하고 순서를 뒤집음
# A,D,F,G 이동, E,C,B 존재 -> E,C,B,G,F,D,A

# 파란색, 벽 바깥:
# 이동 방향을 반대로 하고 한칸 이동, 한번만 바뀜


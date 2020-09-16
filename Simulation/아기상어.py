import sys
sys.stdin = open("input.txt")

# 처음 아기 상어의 크기:2
# 아기상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나 갈 수 없다. 나머지 칸은 갈 수 있다.
# 자신의 크기 보다 작은 물고기만 먹을 수 있다.
# 크기가 같다면 먹을 수는 없지만 지나 갈 수는 있다.

# 먹을 물고기가 없다 -> 끝낸다
# 먹을 물고기가 한마리다 -> 그 물고기 먹으러 간다.
# 한마리 이상이다 -> 가장 가까운 물고기를 먹으러 간다. (가까움 -> 지나야하는 칸의 개수의 최소)
# 거리가 가까운 물고기가 여러개 -> 가장 위. 가장 왼쪽 부터 먹는다
# 이동과 동시에 물고기를 먹고 먹으면 빈칸이 된다.

# 아기상어의 크기는 자신의 크기와 같은 수의 물고리를 먹을 때마다 크기가 1증가
# 크기가 2인애가 3이 될려면 2마리 먹어야 함.

def prin(a):
    for i in a:
        print(i)
    print()

from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0: return False
    elif x >= N or y >= N: return False
    else: return True

def search():
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 9:
                return i,j

def move(x,y,lv):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append((x,y,0))
    matrix[x][y] = 0
    visited[x][y] = 1
    cut = float('inf')
    candidate = []
    while queue:
        x,y,cnt = queue.popleft()
        if cnt > cut:
            break
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny) and not visited[nx][ny]:
                if matrix[nx][ny] == 0 or matrix[nx][ny] == lv:
                    queue.append((nx,ny,cnt+1))
                    visited[nx][ny] = 1
                elif matrix[nx][ny] < lv:
                    cut = cnt
                    candidate.append([nx,ny])
    if candidate:
        candidate.sort()
        matrix[candidate[0][0]][candidate[0][1]] = 0
        return candidate[0][0],candidate[0][1],True,cut+1
    else:
        return -1,-1,False,-1


global N
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
x,y = search()
# 0: 빈칸 , 1~6 물고기의 크기, 9: 아기 상어의 위치 (처음 아기상어의 크기 :2)
dx = [0,0,-1,1]
dy = [1,-1,0,0]
lv,eat = 2,0
time = 0
while True:
    x,y,flag,dif = move(x,y,lv)
    if flag:
        eat += 1
        if lv == eat:
            lv, eat = lv+1,0
    else:
        break
    time += dif
print(time)


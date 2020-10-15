import sys
sys.stdin = open("input.txt")

# 1번말부터 k번 말까지 순서대로 이동
# 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동
# 4개 이상 쌓이는 순간 게임 종료
# 이동하려는칸 :
# 흰색 -> 그칸 이동, 제일 위에 올려놈
# 빨간색 -> 거꾸로 쌓기
# 파란색 ->
def prin(a):
    for i in a:
        print(i)
    print()

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= N : return False
    else : return True

def back(d):
    if d == 1 : return 2
    if d == 2 : return 1
    if d == 3 : return 4
    if d == 4 : return 3

def move():
    # 위치,방향,높이
    for num,arr in enumerate(horse):
        x, y, d, h = arr
        if x == -1 : continue
        if h != 0: continue
        nx,ny = x+dx[d],y+dy[d]
        if not iswall(nx,ny) or matrix[nx][ny] == 2:
            d = back(d)
            horse[num][2] = d
            nx,ny = x+dx[d],y+dy[d]
            if iswall(nx,ny) and matrix[nx][ny] == 0:
                land[nx][ny] = land[nx][ny] + land[x][y]
                land[x][y] = []
                for idx, num in enumerate(land[nx][ny]):
                    d = horse[num][2]
                    horse[num] = [nx, ny, d, idx]

            elif iswall(nx,ny) and matrix[nx][ny] == 1:
                land[nx][ny] = land[nx][ny] + land[x][y][::-1]
                land[x][y] = []
                for idx, num in enumerate(land[nx][ny]):
                    d = horse[num][2]
                    horse[num] = [nx, ny, d, idx]
            else:
                continue

        elif matrix[nx][ny] == 0:
            land[nx][ny] = land[nx][ny] + land[x][y]
            land[x][y] = []
            for idx, num in enumerate(land[nx][ny]):
                d = horse[num][2]
                horse[num] = [nx, ny, d, idx]

        elif matrix[nx][ny] == 1:
            land[nx][ny] = land[nx][ny] + land[x][y][::-1]
            land[x][y] = []
            for idx, num in enumerate(land[nx][ny]):
                d = horse[num][2]
                horse[num] = [nx, ny, d, idx]
        if len(land[nx][ny]) >= 4:
            return True
    else:
        return False

global N,K
N, K = map(int,input().split())
# 0 : 흰색 , 1: 빨간색, 2: 파란색
matrix = [list(map(int,input().split())) for _ in range(N)]
horse = [[-1,-1,-1,-1]]
land = [[[] for _ in range(N)] for _ in range(N)]
for idx in range(K):
    x,y,d = map(int,input().split())
    land[x-1][y-1].append(idx+1)
    horse.append([x-1,y-1,d,len(land[x-1][y-1])-1])
# 우 좌 상 하
dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
for t in range(1,1001):
    if move():
        print(t)
        break
else:
    print(-1)



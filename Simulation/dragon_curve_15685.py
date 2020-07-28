import sys
sys.stdin = open("dragon_curve_15685.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= 101 or y >= 101:
        return False
    else:
        return True
# 끝점에 현재 도형 시계방향으로 돌린것

matrix = [[0 for _ in range(101)] for _ in range(101)]
N = int(input())
info = [list(map(int,input().split())) for _ in range(N)]
# 우 상 좌 하
dx = [0,-1,0,1]
dy = [1,0,-1,0]

for y_start,x_start,d,g in info:
    step = []
    for i in range(g+1):
        if i == 0:
            matrix[x_start][y_start] = 1
            step.append([x_start,y_start])
            if iswall(x_start+dx[d],y_start+dy[d]):
                nx,ny = x_start+dx[d],y_start+dy[d]
                matrix[nx][ny] = 1
                step.append([nx,ny])
        else:
            x_cri,y_cri = step[-1]
            length = len(step)-1
            for st in range(length,-1,-1):
                x,y = step[st]
                x_var,y_var = x - x_cri, y - y_cri
                nx,ny = x_cri+y_var , y_cri-x_var
                if iswall(nx,ny):
                    matrix[nx][ny] = 1
                    step.append([nx,ny])

result = 0
for i in range(100):
    for j in range(100):
        if matrix[i][j] and matrix[i][j+1] and matrix[i+1][j] and matrix[i+1][j+1]:
            result += 1
print(result)

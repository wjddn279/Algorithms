# 5:48
import sys
sys.stdin = open("fish_king_17143.txt")

def prin(a):
    for i in a:
        print(*i)
    print()
# 1. 낚시왕이 열 방향으로 오른쪽으로 한칸 이동
# 2. 낚시왕이 있는 열에 있는 상어 중 땅과 가장 가까운 상어 잡고 상어 사라짐.
# 3. 상어 이동
# 4. 상어가 벽 밖으로 나갈 경우 방향 반대로 바꿔서 이동
# 5. 같은 칸에 상어가 두 마리 있을 경우 크기가 가장 큰 상어만 남는다.
# 6. 낚시왕이 잡은 상의 크기의 합

def iswall(x,y):
    if x < 0 or y < 0: return False
    elif x >= R or y >= C: return False
    else: return True

def fishing(y,result):
    for i in range(R):
        if matrix[i][y][2] != 0:
            val = matrix[i][y][2]
            matrix[i][y] = [0,0,0]
            return result + val
    return result
# 이동방향 : 1 : 위 2: 아래 3: 우 4: 좌
def sharkmoving(x,y,s,d,z):
    matrix[x][y] = [0,0,0]
    for i in range(s):
        nx,ny = x + dx[d], y+dy[d]
        if not iswall(nx,ny):
            if d== 1: d=2
            elif d==2: d=1
            elif d==3: d=4
            elif d==4: d=3
            nx,ny = x + dx[d],y + dy[d]
        x,y = nx,ny
    if new[x][y][2] < z:
        new[x][y][0],new[x][y][1],new[x][y][2] = s,d,z

global R,C
R, C, M  = map(int,input().split())
matrix = [[[0,0,0] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    matrix[r-1][c-1] = [s,d,z]

# r,c,s,d,z = x,y,속력, 이동방향, 크기
# 이동방향 : 1 : 위 2: 아래 3: 우 4: 좌
dx = [0,-1,1,0,0]
dy = [0,0,0,1,-1]
result = 0
for col in range(C):
    result = fishing(col,result)
    new = [[[0,0,0] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if matrix[i][j][2] != 0:
                s,d,z = matrix[i][j]
                sharkmoving(i,j,s,d,z)
    matrix = new
print(result)
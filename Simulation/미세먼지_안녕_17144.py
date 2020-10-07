import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)
    print()

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= M : return False
    elif matrix[x][y] == -1 : return False
    else : return True

def ready():
    for x,y,temp in mungi:
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if iswall(nx,ny):
                matrix[nx][ny] += temp//5
                matrix[x][y] -= temp//5
                if matrix[x][y] < 0:
                    matrix[x][y] = 0

def upclean(a):
    temp = 0
    for j in range(1,M):
        t = matrix[a][j]
        matrix[a][j] = temp
        temp = t
    for j in range(a-1,-1,-1):
        t = matrix[j][M-1]
        matrix[j][M-1] = temp
        temp = t
    for j in range(M-2,-1,-1):
        t = matrix[0][j]
        matrix[0][j] = temp
        temp = t
    for j in range(1,a):
        t = matrix[j][0]
        matrix[j][0] = temp
        temp = t
    matrix[a][0] = -1

def downclean(a):
    temp = 0
    for j in range(1,M):
        t = matrix[a][j]
        matrix[a][j] = temp
        temp = t
    for j in range(a+1,N):
        t = matrix[j][M-1]
        matrix[j][M-1] = temp
        temp = t
    for j in range(M-2,-1,-1):
        t = matrix[N-1][j]
        matrix[N-1][j] = temp
        temp = t
    for j in range(N-2,a,-1):
        t = matrix[j][0]
        matrix[j][0] = temp
        temp = t
global N,M
N, M, T = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
robot = [i for i in range(N) if matrix[i][0] == -1]
mungi = [(i,j,matrix[i][j]) for i in range(N) for j in range(M) if matrix[i][j] > 0]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for _ in range(T):
    ready()
    upclean(robot[0])
    downclean(robot[1])
    mungi = [(i,j,matrix[i][j]) for i in range(N) for j in range(M) if matrix[i][j] > 0]
answer = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] > 0:
            answer += matrix[i][j]
print(answer)




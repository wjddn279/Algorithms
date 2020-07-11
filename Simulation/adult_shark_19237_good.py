# 1:위 2:아래 3:왼쪽 4:오른쪽
# 냄새가 없는 칸의 방향 다음 냄새가 있는 칸의 방향
# 그중 우선순위 따름
# 상어가 만나면 가장 작은 번호 상어만 남는다
import sys
sys.stdin = open('shark.txt')

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()
def wall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= len(matrix) or y >= len(matrix):
        return False
    else:
        return True
def solve(cnt):
    # 한차례 지나서 냄새 하나 빠짐
    visited = []
    # temp = (상어번호, 그 칸의 냄새 남은 시간, 방향, 냄새 주인 상어번호)
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            yes_smell,no_smell = [],[]
            if sharkmap[i][j][0] > 0 and (i,j) not in visited:
                for k in range(4):
                    idx = rule[sharkmap[i][j][0]-1][sharkmap[i][j][2]-1][k]
                    dx,dy = code[idx-1]
                    nx,ny = i+dx,j+dy
                    if wall(nx,ny):
                        if sharkmap[nx][ny][3] == 0:
                            no_smell.append((nx,ny,idx))
                        elif sharkmap[nx][ny][3] == sharkmap[i][j][3]:
                            yes_smell.append((nx,ny,idx))
                if len(no_smell) != 0:
                    nx,ny,idx = no_smell[0]
                else:
                    nx,ny,idx = yes_smell[0]
                if sharkmap[nx][ny][0] !=0:
                    if sharkmap[nx][ny][0] > sharkmap[i][j][0]:
                        sharkmap[nx][ny] = [sharkmap[i][j][0],K,idx,sharkmap[nx][ny][3]]
                else:
                    sharkmap[nx][ny] = [sharkmap[i][j][0], K, idx,sharkmap[nx][ny][3]]
                sharkmap[i][j][0] = 0
                sharkmap[i][j][2] = 0
                visited.append((nx,ny))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if sharkmap[i][j][0] != 0:
                sharkmap[i][j][3] = sharkmap[i][j][0]
    number = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if sharkmap[i][j][1] > 0 and (i,j) not in visited:
                temp = sharkmap[i][j][1]
                sharkmap[i][j][1] = temp-1
                if sharkmap[i][j][1] == 0:
                    sharkmap[i][j][3] = 0
            if sharkmap[i][j][0] > 0:
                number += 1
    return cnt+1,number




global K
N,M,K = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
sharkmap = []
start_direction = list(map(int,input().split()))
code = [(-1,0),(1,0),(0,-1),(0,1)]
for i in range(N):
    temp = []
    for j in range(N):
        if matrix[i][j] != 0:
            temp.append([matrix[i][j],K,start_direction[matrix[i][j]-1],matrix[i][j]])
        else:
            temp.append([0,0,0,0])
    sharkmap.append(temp)
rule = []
for i in range(M):
    dic = {}
    for j in range(4):
        dic[j] = list(map(int,input().split()))
    rule.append(dic)
cnt = 0
for iteration in range(1,1001):
    cnt,number = solve(cnt)
    if number == 1:
        print(iteration)
        break
else:
    print(-1)
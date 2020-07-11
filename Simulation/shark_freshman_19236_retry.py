import sys
sys.stdin = open("shark_freshman.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

from _collections import deque
from copy import deepcopy

def search():
    for i in range(4):
        for j in range(4):
            location[mapping[i][j][0]] = (i,j)

def iswall(x,y,matrix):
    if x < 0 or y < 0 :
        return False
    elif x >= 4 or y >= 4:
        return False
    elif matrix[x][y][0] == 100:
        return False
    else:
        return True

def generate_shark():
    temp = mapping[0][0][0]
    location[temp] = (-1,-1)
    mapping[0][0][0] = 100
    queue.append((0,0,[temp],deepcopy(mapping),deepcopy(location)))

def fish_moving(matrix,location):
    # 상어는 100으로, 원래 있던 놈의 위치는 0으로 초기화
    for i in range(1,17):
        if location[i] == (-1,-1):
            continue
        # i 번쨰 상어의 현재 위치, 방향
        x,y = location[i]
        direction = matrix[x][y][1]
        # 물고기가 다 이동하고 상어가 이동
        # 1번 물고기 부터 순서대로 이동하고 이동 위치에 다른 물고기가 있다면 위치 교환
        # 물고기가 가는 방향에 상어가 있으면 45도 반시계 회전
        nx,ny = x+dx[direction%9-1], y+dy[direction%9-1]
        # iswall 만족하면 탈출
        while not iswall(nx,ny,matrix):
            direction += 1
            nx = x+dx[direction%9-1]
            ny = y+dy[direction%9-1]
        # 물고기 위치 바꾸기
        if matrix[nx][ny][0] == 0:
            location[matrix[x][y][0]] = (nx,ny)
        else:
            location[matrix[x][y][0]],location[matrix[nx][ny][0]] = location[matrix[nx][ny][0]],location[matrix[x][y][0]]
        # 바뀔 위치 ,원래 위치
        matrix[nx][ny],matrix[x][y] = matrix[x][y], matrix[nx][ny]
        matrix[nx][ny][1] = direction%9

    return matrix, location
# 위,위왼,왼,아래왼,아래,아래오,오,위오

def shark_moving():
    # x , y , 방향 , 먹은 물고기
    while queue:
        x,y,cnt,matrix,location = queue.popleft()
        direc = matrix[x][y][1]
        matrix, location = fish_moving(matrix,location)
        for k in range(1,4):
            nx,ny = x + k * dx[direc-1], y + k * dy[direc-1]
            if not iswall(nx,ny,matrix):
                if sum(cnt) > result[0]:
                    result[0] = sum(cnt)
                    break
            else:
                if matrix[nx][ny][0] == 0:
                    continue
                mapping = deepcopy(matrix)
                loca = deepcopy(location)
                # 상어한테 잡아 먹혀서 물고기 없어짐
                loca[mapping[nx][ny][0]] = (-1,-1)
                # 물고기 먹었으니까 합 증가 하고
                # 그 자리에 상어 값이 들어감
                temp = mapping[nx][ny][0]
                mapping[nx][ny][0] = mapping[x][y][0]
                # 상어 방향 먹은 물고기 방향
                # 물고기가 빈칸이라면(없다면) 방향 그대로
                mapping[x][y] = [0,0]
                queue.append((nx,ny,cnt+[temp],mapping,loca))


dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]
mapping = []
result = [0]
for i in range(4):
    temp = list(map(int,input().split()))
    arr = []
    for j in range(4):
        tem = [temp[2*j],temp[2*j+1]]
        arr.append(tem)
    mapping.append(arr)
# 물고기의 위치
location = [0 for _ in range(17)]
queue = deque()
search()
generate_shark()
shark_moving()
print(result[0])

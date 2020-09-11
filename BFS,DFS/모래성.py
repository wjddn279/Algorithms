import sys
sys.stdin = open("input.txt")

def prin(a):
    for i in a:
        print(i)
    print()
# 튼튼함 1~9
# 격자 주변 8방향을 봐서 모래성이 쌓여 있지 않은 부분의 개수 >= 튼튼함   -> 무너짐
# 모래성이 무너지면 격자는 쌓여있지 않은 것으로 취급
# 더이상 모양이 변하지 않게 되려면 파도가 몇번 쳐야 하는가
from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= M : return False
    else: return True

def init():
    queue= deque()
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                queue.append((i,j))
    return queue

def solve(queue):
    next = deque()
    while queue:
        x, y = queue.popleft()
        for k in range(8):
            nx, ny = x + dx[k], y + dy[k]
            if iswall(nx, ny):
                if matrix[nx][ny] != 0:
                    matrix[nx][ny] -= 1
                    if matrix[nx][ny] == 0:
                        next.append((nx, ny))
    return next
global N,M
N, M = map(int,input().split())
# 1~9의 숫자 혹은 '.' 빈 모래
matrix = []
for i in range(N):
    temp = list(input())
    for j in range(M):
        if temp[j] == '.':
            temp[j] = 0
        else:
            temp[j] = int(temp[j])
    matrix.append(temp)
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
queue = init()
result = -1
while queue:
    result += 1
    queue = solve(queue)
print(result)


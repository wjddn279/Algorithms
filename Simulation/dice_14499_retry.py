import sys
sys.stdin = open("dice.txt")

from _collections import deque


def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= N or y >= M:
        return False
    else:
        return True

# N: 세로크기 M: 가로크기 x,y : 주사위를 놓은 곳의 좌표 , K : 명령의 갯수
global N,M
N, M, x, y, K = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
# 1: 동 2: 서 3: 북 4: 남
orders = list(map(int,input().split()))
print(orders)
dx = [0,0,-1,1]
dy = [1,-1,0,0]

# 이동한 칸의 값이 0 이면 주사위 바닥면 의 값 복제
# 0 이 아닌경우 칸에 쓰여 있는 수가 주사위 바닥면으로 복제
# dice_tree : 0~3 : 현 위치의 동서북남 번호 4: 맞은편 번호
dice_tree = [[],[3,4,2,5],[3,4,6,1],[6,1,2,5],[1,6,2,5],[3,4,1,6],[3,4,5,2]]
dice_cross = [0,6,5,4,3,2,1]
dice = [0 for _ in range(7)]
now = 1
direction = 0
#  6 1 2 5 -> 5 2 6 1
# 2의 동쪽이 3 -> 3의 서쪽은 2 다
for order in orders:


    nx = x + dx[order-1]
    ny = y + dy[order-1]
    if not iswall(nx,ny):
        continue
    next = dice_tree[now][order-1]
    
    if matrix[nx][ny] != 0:
        dice[now] = matrix[nx][ny]
        matrix[nx][ny] = 0
    else:
        matrix[nx][ny] = dice[now]
    print(now)
    # print(dice[dice_tree[now][4]])
    print(dice)
    x,y = nx,ny



    # 5 6 2 3 2

import sys
sys.stdin = open("rotate_circle_17822.txt")

from _collections import deque
from copy import deepcopy

N,M,T = map(int,input().split())
# 각 원판에 적혀있는 수 순서대로
matrix = [[]] + [deque(map(int,input().split())) for _ in range(N)]
xdk = [list(map(int,input().split())) for _ in range(T)]
# 시계 방향으로 돈다.
for x,d,k in xdk:

    total = 0
    number = 0
    if d == 0:
        for i in range(x,N+1,x):
            queue = []
            for _ in range(k):
                temp = matrix[i].pop()
                queue.append(temp)

            matrix[i] = deque(queue[::-1]) + matrix[i]
    else:
        for i in range(x,N+1,x):
            queue = deque()
            for _ in range(k):
                temp = matrix[i].popleft()
                matrix[i].append(temp)

    flag = False
    # 새로운 matrix의 복사본을 만드는 이유?


    # 4 4
    # 4
    # 4
    # 이경우 안쪽에서
    fake = deepcopy(matrix)
    for n in range(1,N+1):
        for m in range(M):
            if matrix[n][m] != 0:
                temp = matrix[n][m]

                # 위 아래 껍질 비교
                if n == 1:
                    up,down = 2,-1
                elif n == N:
                    up,down = -1,N-1
                else:
                    up,down = n+1,n-1

                if n != N and temp == matrix[up][m]:
                    fake[n][m], fake[up][m] = 0, 0
                    flag = True
                if n != 1 and temp == matrix[down][m]:
                    fake[n][m], fake[down][m] = 0, 0
                    flag = True

                # 좌우 껍질 비교
                if m == 0:
                    right,left = 1,M-1
                elif m == M-1:
                    right,left = 0,M-2
                else:
                    right,left = m+1,m-1

                if temp == matrix[n][left]:
                    fake[n][m], fake[n][left] = 0, 0
                    flag = True
                if temp == matrix[n][right]:
                    fake[n][m], fake[n][right] = 0, 0
                    flag = True
    if not flag:
        for n in range(1, N + 1):
            for m in range(M):
                if matrix[n][m] != 0:
                    total += matrix[n][m]
                    number += 1
        if total == 0 and number == 0:
            break
        avg = total/number
        for n in range(1, N + 1):
            for m in range(M):
                if matrix[n][m] != 0:
                    if matrix[n][m] < avg:
                        matrix[n][m] += 1
                    elif matrix[n][m] > avg:
                        matrix[n][m] -= 1
    else:
        matrix = fake

total = 0
for n in range(1, N + 1):
    for m in range(M):
        if matrix[n][m] != 0:
            total += matrix[n][m]
print(total)



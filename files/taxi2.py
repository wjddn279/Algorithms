import sys
from _collections import deque
sys.stdin = open("taxi.txt")

drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]

def iswall(row, col):
    if row < 0 or row >= N:
        return False
    if col < 0 or col >= N:
        return False
    return True

def close_distance(row, col):
    global k
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[row-1][col-1] = 1
    queue = deque()
    queue.append((row-1, col-1))
    chk = N*N
    memo = []
    while queue:
        r, c = queue.popleft()
        if visited[r][c] > chk:
            k -= chk
            if len(memo) == 1:
                idx = memo[0]
            else:
                row, col = passenger[memo[0]]
                for i in range(1, len(memo)):
                    if passenger[memo[i]][0] < row:
                        idx = memo[i]
                    elif passenger[memo[i]][0] == row and passenger[memo[i]][1] < col:
                        idx = memo[i]
            move(idx)
            next_row, next_col = destination[idx]
            passenger[idx] = (-1, -1)
            destination[idx] = (-1, -1)
            return next_row + 1, next_col + 1

        for i in range(4):
            test_r = r + drow[i]
            test_c = c + dcol[i]
            if iswall(test_r, test_c):
                if visited[test_r][test_c] == 0 and maplist[test_r][test_c] != 1:
                    visited[test_r][test_c] = visited[r][c] + 1
                    queue.append((test_r, test_c))
                    for j in range(len(passenger)):
                        if passenger[j] == (test_r, test_c):
                            if visited[r][c] <= chk:
                                chk = visited[r][c]
                                memo.append(j)
    return -1, -1

def move(n):
    global k
    visited2 = [[0 for _ in range(N)] for _ in range(N)]
    visited2[passenger[n][0]][passenger[n][1]] = 1
    que = deque()
    que.append(passenger[n])
    while que:
        r, c = que.popleft()
        for i in range(4):
            test_r = r + drow[i]
            test_c = c + dcol[i]
            if iswall(test_r, test_c):
                if visited2[test_r][test_c] == 0 and maplist[test_r][test_c] != 1:
                    visited2[test_r][test_c] = visited2[r][c] + 1
                    que.append((test_r, test_c))
                    if destination[n] == (test_r, test_c):
                        if k >= visited2[r][c]:
                            k += visited2[r][c]
                        else:
                            k = -1
                        return


N, M, k = map(int, input().split())
maplist = [list(map(int, input().split())) for _ in range(N)]
st_row, st_col = map(int, input().split())
passenger = []
destination = []

for _ in range(M):
    st_r, st_c, ed_r, ed_c = map(int, input().split())
    passenger.append((st_r - 1, st_c - 1))
    destination.append((ed_r - 1, ed_c - 1))
for _ in range(M):
    st_row, st_col = close_distance(st_row, st_col)
    if (st_row, st_col) == (-1, -1):
        k = -1
        break
    if k < 0:
        k = -1
        break

print(k)
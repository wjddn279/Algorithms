from collections import deque
import sys
sys.stdin = open("taxi.txt")

def find_customer(taxi_row, taxi_col):

    queue = deque()
    queue.append((taxi_row, taxi_col))
    chk = [[0] * N for _ in range(N)]
    chk[taxi_row][taxi_col] = 1
    min_dist = 987654321
    min_row, min_col, min_cust = 987654321, -1, -1
    while queue:

        row, col = queue.popleft()

        if maplist[row][col] > 1 and chk[row][col] <= min_dist:
            min_dist = chk[row][col]
            if min_row > row:
                min_row = row
                min_col = col
                min_cust = maplist[row][col]
            elif min_row == row and min_col > col:
                min_col = col
                min_cust = maplist[row][col]


        for idx in range(4):
            next_row = row + dy[idx]
            next_col = col + dx[idx]

            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
                continue
            if chk[next_row][next_col] or maplist[next_row][next_col] == 1:
                continue

            chk[next_row][next_col] = chk[row][col] + 1
            queue.append((next_row, next_col))

    if min_col >= 0:
        maplist[min_row][min_col] = 0

    return min_row, min_col, min_cust, min_dist-1


def find_dest(row, col, cust_num):
    queue = deque()
    queue.append((row, col))

    chk = [[0] * N for _ in range(N)]
    chk[row][col] = 1


    while queue:
        row, col = queue.popleft()

        if maplist_dest[row][col] == cust_num:
            maplist_dest[row][col] = 0
            return row, col, chk[row][col]-1

        for idx in range(4):
            next_row = row + dy[idx]
            next_col = col + dx[idx]

            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
                continue
            if chk[next_row][next_col] or maplist_dest[next_row][next_col] == 1:
                continue

            chk[next_row][next_col] = chk[row][col] + 1
            queue.append((next_row, next_col))

    return -1, -1, -1

N, M, cur_fuel = map(int, input().split())

maplist = [list(map(int, input().split())) for _ in range(N)]
maplist_dest = [[0] * N for _ in range(N)]

for i in range(N):
    maplist_dest[i] = list(maplist[i])

taxi_row, taxi_col = map(int, input().split())
taxi_row -= 1
taxi_col -= 1
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


for i in range(2, M+2):
    sty, stx, edy, edx = map(int, input().split())
    maplist[sty-1][stx-1] = i
    maplist_dest[edy-1][edx-1] = i



for _ in range(M):

    if maplist[taxi_row][taxi_col] > 1:
        customer_num = maplist[taxi_row][taxi_col]
        maplist[taxi_row][taxi_col] = 0
        dist = 0
    else:
        taxi_row, taxi_col, customer_num, dist = find_customer(taxi_row, taxi_col)

    cur_fuel -= dist
    if cur_fuel < 0 or customer_num < 0:
        cur_fuel = -1
        break

    taxi_row, taxi_col, dist = find_dest(taxi_row, taxi_col, customer_num)

    cur_fuel -= dist
    if cur_fuel < 0 or taxi_row < 0:
        cur_fuel = -1
        break
    else:
        cur_fuel += dist * 2

print(cur_fuel)


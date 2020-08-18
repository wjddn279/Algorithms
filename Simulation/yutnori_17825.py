import sys
sys.stdin = open("input.txt")

from itertools import product


data = list(map(int,input().split()))
load = []
load.append(list(range(0,41,2)) + [-1 for _ in range(5)])
load.append([10,13,16,19,25,30,35,40] + [-1 for _ in range(5)])
load.append([20,22,24,25,30,35,40] + [-1 for _ in range(5)])
load.append([30,28,27,26,25,30,35,40] + [-1 for _ in range(5)])
result = 0

for route in product(range(4),repeat=10):
    val = 0
    visited = [[0, 0] for _ in range(4)]
    # 위치 , 노선
    for idx,seq in enumerate(route):
        if visited[seq][0] == -1:
            val = 0
            break
        visited[seq][0] += data[idx]
        if load[visited[seq][1]][visited[seq][0]] != -1:
            val += load[visited[seq][1]][visited[seq][0]]
        # 도착했어
        if load[visited[seq][1]][visited[seq][0]] == -1:
            visited[seq][0] = -1
        elif load[visited[seq][1]][visited[seq][0]] == 10:
            visited[seq][0] = 0
            visited[seq][1] = 1
        elif load[visited[seq][1]][visited[seq][0]] == 20:
            visited[seq][0] = 0
            visited[seq][1] = 2
        elif visited[seq][1] == 0 and load[visited[seq][1]][visited[seq][0]] == 30:
            visited[seq][0] = 0
            visited[seq][1] = 3
        for i in range(4):
            if i != seq and visited[seq] != [0,0] and visited[seq][0] != -1:

                val = 0
                break
        if route == (0, 0, 1, 0, 2, 2, 2, 0, 2, 2):
            print(visited)

    result = max(result,val)

print(result)
# 5 1 2 3 4 5 5 3 2 4
# 0 0 1 0 2 2 2 0 2 2)

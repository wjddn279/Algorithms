import sys
sys.stdin = open("ACM_craft.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()
# 2,3번 건물 동시에 짓는거 가능

# 첫째줄: N 건물의 갯수, K : 건물간 건설순서규칙 총 개수
# 둘째줄: 건물당 건설에 걸리는 시간 D
# 셋째줄~K+2: 순서

from _collections import deque

T = int(input())

for _ in range(T):
    N, K = map(int,input().split())
    time = [0]+list(map(int,input().split()))
    matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
    ind = [0 for _ in range(N+1)]
    stack = []
    flag = False
    for _ in range(K):
        x,y = map(int,input().split())
        matrix[x][y] = 1
        ind[y] += 1
    target = int(input())
    build_time = [[0 for _ in range(N+1)] for _ in range(N+1)]
    temp = [0 for _ in range(N+1)]
    for i in range(1,N+1):
        if ind[i] == 0:
            stack.append((i,1))
            build_time[i][1] = time[i]
            if i == target:
                flag = True
    if flag:
        print(time[target])
    else:
        queue = deque(stack)
        while queue:
            x,cnt = queue.popleft()
            if x == target:
                break
            for i in range(1,N+1):
                if matrix[x][i] == 1:
                    ind[i] -= 1
                    if temp[i] < sum(build_time[x]):
                        temp[i] = sum(build_time[x])
                    if ind[i] == 0:
                        queue.append((i,cnt+1))
                        build_time[i][cnt+1] = time[i]
                        build_time[i][cnt] = temp[i]
        print(sum(build_time[target]))
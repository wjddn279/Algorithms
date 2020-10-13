import sys
sys.stdin = open("input.txt")


from _collections import deque

T = int(input())

def cycle(x,d):
    if d == 1:
        data[x].appendleft(data[x].pop())
    else:
        data[x].append(data[x].popleft())

def rotation(x,d):
    stack = [(x,d)]
    queue = deque()
    queue.append((x,d))
    visited[x] = 1
    while queue:
        x,d = queue.popleft()
        for idx,arr in enumerate(order[x]):
            next,pos = arr
            if data[x][look[x][idx]] != data[next][pos] and not visited[next]:
                queue.append((next,-1*d))
                stack.append((next,-1*d))
                visited[next] = 1
    while stack:
        x,d = stack.pop()
        cycle(x,d)

for test_case in range(1,T+1):
    N = int(input())
    data = [deque(map(int,input().split())) for _ in range(4)]
    rotate = [list(map(int,input().split())) for _ in range(N)]
    order = {0:[[1,6]],1:[[0,2],[2,6]],2:[[1,2],[3,6]],3:[[2,2]]}
    look = {0:[2],1:[6,2],2:[6,2],3:[6]}
    # 시계 방향 상 우 하 좌
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    for c,d in rotate:
        visited = [0,0,0,0]
        rotation(c-1,d)
    answer = 0
    for idx,arr in enumerate(data):
        answer += pow(2,idx) * arr[0]
    print('#{} {}'.format(test_case,answer))
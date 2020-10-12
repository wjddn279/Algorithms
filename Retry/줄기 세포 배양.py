# 1시 30분
import sys
sys.stdin = open("input.txt")

# 활성화 된 줄기세포는 첫 1시간동안 상하좌우 네방향으로 번식
# 이미 세포가 있는 경우 번식 x
# 동시에 같은 셀로 번식하는 경우 값이 큰 세포가 번식
from _collections import deque
import heapq

T = int(input())

def search():
    for i in range(N):
        for j in range(M):
            if matrix[i][j]:
                visited[(i,j)] = matrix[i][j]
                queue.append((matrix[i][j],i,j,2*matrix[i][j]))

def time(now):
    temp = {}
    # 전에 활성한 애들 번식
    length = len(action)
    for _ in range(length):
        t,x,y,e = action.popleft()
        if now == t+1:
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if (nx,ny) not in visited:
                    if (nx,ny) not in temp:
                        temp[(nx,ny)] = visited[(x,y)]
                    elif visited[(x,y)] > temp[(nx,ny)]:
                        temp[(nx,ny)] = visited[(x,y)]
        if now == e:
            continue
        else:
            action.append((t,x,y,e))
    for pos,val in temp.items():
        x,y = pos
        heapq.heappush(queue,(now+val,x,y,now+val+val))
        visited[(x,y)] = val

    #  활성한 애들 골라내기
    while queue and queue[0][0] <= now:
        t,x,y,e = heapq.heappop(queue)
        action.append((t,x,y,e))


for test_case in range(1,T+1):
    global N,M,K
    N, M, K = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    # 전체 왔다갔다
    visited = {}
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    # 비활성 상태, 활성 상태
    queue,action = [], deque()
    search()
    heapq.heapify(queue)
    for t in range(1,K+1):
        time(t)
    print(len(queue)+len(action))
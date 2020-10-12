# 3시 30분
import sys
sys.stdin = open("input.txt")


# -1000 0 -> 1000 0
# 1000 0 -> 1000 2000
# 0 1000 -> 0 2000
# 0 -1000 ->
# 원자가 충돌하면 원자들은 각자 보유한 에너지 방출 및 소멸

from _collections import deque

T = int(input())

def iswall(x,y):
    if x < -1000 or y < -1000: return False
    elif x > 1000 or y > 1000: return False
    else: return True

def crash(d):
    if d == 0 : return 1
    if d == 1 : return 0
    if d == 2 : return 3
    if d == 3 : return 2

for test_case in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    queue = deque()
    for x,y,d,e in data:
        queue.append((x,y,d,e))
    # 상,하,좌,우
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    result = 0
    while queue:
        visited = {}
        while queue:
            x,y,d,e = queue.popleft()
            nx,ny = x+dx[d],y+dy[d]
            nnx,nny = nx+dx[d],ny+dy[d]
            if (x,y) in visited and d == crash(visited[(x,y)][0]) and visited[(x,y)][2] == 0:
                a, b, c = visited[(x, y)]
                visited[(x,y)] = [a, b + e, c + 1]
                continue
            if iswall(nx,ny):
                if (nx,ny) in visited:
                    a,b,c = visited[(nx,ny)]
                    visited[(nx,ny)] = [a,b+e,c+1]
                else:
                    visited[(nx,ny)] = [d,e,0]

        for pos,arr in visited.items():
            x,y = pos
            d,e,c = arr
            if c == 0:
                queue.append((x,y,d,e))
            else:
                result += e
    print('#{} {}'.format(test_case,result))


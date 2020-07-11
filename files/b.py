import sys
from _collections import deque
sys.stdin = open("input9.txt")

def bfs(start,end):
    if start == end:
        return 0
    queue = deque()
    queue.append((start,0))
    while queue:
        now,cnt = queue.popleft()
        for i in can:
            nx = now + i
            if nx == end:
                return cnt + 1
            elif nx > 0 and nx <= h and visited[nx] == 0:
                queue.append((nx,cnt+1))
                visited[nx] = cnt + 1
    return 'use the stairs'

h,start,end,up,down = map(int,input().split())
visited = [0 for _ in range(h+1)]
can = [up, -1 * down]
print(bfs(start,end))
# 하나씩 해보면 된다

def prin(a):
    for i in a:
        print(i)
    print()

from itertools import permutations
from _collections import deque

def solution(board, r, c):
    answer = [float('inf')]
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    def rec(k,nx,ny,subsum,delete):
        if k == len(cards):
            if subsum < answer[0]:
                answer[0] = subsum
        else:
            k1 = location[seq[k]]
            rec(k+1,k1[1][0],k1[1][1],subsum+move(nx,ny,k1[0][0],k1[0][1],delete)+move(k1[0][0],k1[0][1],k1[1][0],k1[1][1],delete),delete+[board[k1[1][0]][k1[1][1]]])
            k1 = location[seq[k]][::-1]
            rec(k+1,k1[1][0],k1[1][1],subsum+move(nx,ny,k1[0][0],k1[0][1],delete)+move(k1[0][0],k1[0][1],k1[1][0],k1[1][1],delete),delete+[board[k1[1][0]][k1[1][1]]])

    def iswall(x,y):
        if x < 0 or y < 0: return False
        elif x >= 4 or y >= 4: return False
        else: return True

    def move(sx,sy,ex,ey,delete):
        if sx == ex and sy == ey:
            return 1
        visited = [[float('inf') for _ in range(4)] for _ in range(4)]
        visited[sx][sy] = 0
        queue = deque()
        queue.append((sx,sy,0))

        while queue:
            x,y,cnt = queue.popleft()
            # ctrl 이동
            for i in range(4):
                for k in range(1,5):
                    nx,ny = x+ k * dx[i],y + k * dy[i]
                    if nx == ex and ny == ey:
                        return cnt + 2
                    if not iswall(nx,ny):
                        if k != 1 and visited[x+(k-1)*dx[i]][y+(k-1)*dy[i]] > cnt + 1:
                            queue.append((x+(k-1)*dx[i],y+(k-1)*dy[i],cnt+1))
                            visited[x+(k-1)*dx[i]][y+(k-1)*dy[i]] = cnt+1
                        break
                    if board[nx][ny] and board[nx][ny] not in delete:
                        if visited[nx][ny] > cnt + 1:
                            queue.append((nx,ny,cnt+1))
                            visited[nx][ny] = cnt + 1
                        break
            # 그냥 이동
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if nx == ex and ny == ey:
                    return cnt + 2
                if iswall(nx,ny) and visited[nx][ny] > cnt+1:
                    queue.append((nx,ny,cnt+1))
                    visited[nx][ny] = cnt + 1

    cards = []
    location = [[] for _ in range(7)]
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                if board[i][j] not in cards:
                    cards.append(board[i][j])
                location[board[i][j]].append((i,j))
    per = list(permutations(cards,len(cards)))

    for seq in per:
        rec(0,r,c,0,[])
    return answer[0]

print(solution(	[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],1,0))
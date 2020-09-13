from _collections import deque

def solution(maze):
    answer = 0
    N = len(maze)
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    priority = {0:[3,0,2,1],3:[1,3,0,2],1:[2,1,3,0],2:[0,2,1,3]}

    def iswall(x,y):
        if x < 0 or y < 0: return False
        elif x >= N or y >= N: return False
        else : return True

    def move():
        queue = deque()
        # x,y,dir
        queue.append((0,0,2,0))
        while queue:
            x,y,dir,cnt = queue.popleft()
            for i in priority[dir]:
                nx,ny = x+dx[i],y+dy[i]
                if iswall(nx,ny) and not maze[nx][ny]:
                    if nx == N-1 and ny == N-1:
                        return cnt+1
                    queue.append((nx,ny,i,cnt+1))
                    break
    answer = move()

    return answer

print(solution(	[[0, 1, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0], [0, 1, 0, 0, 1, 0], [0, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0]]))
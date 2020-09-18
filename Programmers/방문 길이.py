def prin(a):
    for i in a:
        print(i)
    print()

def solution(dirs):
    def iswall(x,y):
        if x < -5 or y < -5: return False
        elif x > 5 or y > 5: return False
        else: return True

    def rev(dir):
        if dir == 0: return 1
        if dir == 1: return 0
        if dir == 2: return 3
        if dir == 3: return 2

    answer = 0
    direction = {'L':(-1,0,0),'R':(1,0,1),'U':(0,1,2),'D':(0,-1,3)}
    visited = [[[0,0,0,0] for _ in range(11)] for _ in range(11)]
    x,y = 0,0
    for dir in dirs:
        dx,dy,idx = direction[dir]
        nx,ny = x+dx,y+dy
        if iswall(nx,ny):
            if not visited[x+5][y+5][idx]:
                visited[x+5][y+5][idx] = 1
                visited[nx+5][ny+5][rev(idx)] = 1
                answer += 1
            x,y = nx,ny
    return answer

print(solution("ULURRDLLU"))
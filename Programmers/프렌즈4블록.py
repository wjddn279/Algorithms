from _collections import deque

def prin(a):
    for i in a:
        print(i)
    print()

def solution(n, m, boa):
    board = [list(b) for b in boa]
    answer = 0
    dx = [0,1,1]
    dy = [1,1,0]

    def iswall(x,y):
        if x < 0 or y < 0: return False
        elif x >= n or y >= m : return False
        elif board[x][y] == -1: return False
        else: return True

    def bomb():
        temp = 0
        stack = []
        for x in range(n):
            for y in range(m):
                if board[x][y] != -1:
                    for i in range(3):
                        nx,ny = x+dx[i],y+dy[i]
                        if not iswall(nx,ny) or board[nx][ny] != board[x][y]:
                            break
                    else:
                        stack.append((x,y))
        while stack:
            x,y = stack.pop()
            if board[x][y] != -1:
                board[x][y] = -1
                temp += 1
            for i in range(3):
                nx,ny = x+dx[i],y+dy[i]
                if board[nx][ny] != -1:
                    board[nx][ny] = -1
                    temp += 1
        return temp

    def move():
        for y in range(m):
            for i in range(n-1,-1,-1):
                for j in range(n-1,i,-1):
                    if board[j][y] == -1:
                        board[i][y],board[j][y] = board[j][y],board[i][y]

    temp = 1
    while temp:
        temp = bomb()
        answer += temp
        move()
    return answer

print(solution(6,6,	["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
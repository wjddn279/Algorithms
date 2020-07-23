import sys
sys.stdin = open("17779.txt")

def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= N or y >= N:
        return False
    else:
        return True

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()
def ready(x,y,result):
    for d1 in range(1,N):
        for d2 in range(1,N):
            if iswall(x+d1,y-d1) and iswall(x+d2,y+d2) and iswall(x+d1+d2,y-d1+d2) and iswall(x+d2+d1,y+d2-d1):
                result = min(solve(x,y,d1,d2),result)
            else:
                continue
    return result

def solve(x,y,d1,d2):
    value = [0 for _ in range(5)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for r in range(N):
        temp = r-x
        if temp > d1:
            left = y -d1 + temp - d1
        else:
            left = y - temp
        if temp > d2:
            right =  y + d2 - (temp -d2)
        else:
            right = y +temp
        for c in range(N):
            if x <= r <= x + d1 +d2 and left <= c <= right:
                value[4] += matrix[r][c]
                visited[r][c] = 5
            elif 0 <= r < x+d1 and 0 <= c <= y:
                value[0] += matrix[r][c]
                visited[r][c] = 1
            elif 0 <= r <= x+d2 and y < c < N:
                value[1] += matrix[r][c]
                visited[r][c] = 2
            elif x+d1 <= r < N and 0 <= c < y-d1+d2 :
                value[2] += matrix[r][c]
                visited[r][c] = 3
            elif x+d2 < r < N and y-d1+d2 <= c < N:
                value[3] += matrix[r][c]
                visited[r][c] = 4
    result = max(value) - min(value)
    return result
global N
N = int(input())
matrix = [list(map(int,input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
value = [0 for _ in range(5)]
result = 987654321
for i in range(1,N):
    for j in range(1,N):
        result = ready(i,j,result)
print(result)
import sys
sys.stdin = open("input.txt")

def iswall(x,y):
    if x < 0 or y < 0 : return False
    elif x >= N or y >= M : return False
    else: return True

global N,M
N, M = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]
result = 0
dx = [[[0,0,0,0],[0,1,2,3]],
      [[0,0,1,1]],[[0,1,2,2],[0,0,0,1],[0,0,1,2],[0,1,1,1],[0,1,2,2],[0,1,1,1],[0,0,1,2],[0,0,0,1]],
      [[0,1,1,2],[0,0,1,1],[0,1,1,2],[0,0,1,1]],
      [[0,0,0,1],[0,1,1,2],[0,1,1,1],[0,1,1,2]]]
dy = [[[0,1,2,3],[0,0,0,0]],
      [[0,1,0,1]],
      [[0,0,0,1],[0,1,2,0],[0,1,1,1],[2,0,1,2],[1,1,0,1],[0,0,1,2],[0,1,0,0],[0,1,2,2]],
      [[0,0,1,1],[1,2,0,1],[1,1,0,0],[0,1,1,2]],
      [[0,1,2,1],[1,0,1,1],[1,0,1,2],[0,0,1,0]]
      ]

# 1번 모양
for k in range(5):
    for shape in range(len(dx[k])):
        for x in range(N):
            for y in range(M):
                temp = 0
                for i in range(4):
                    nx,ny = x+dx[k][shape][i],y+dy[k][shape][i]
                    if iswall(nx,ny):
                        temp += matrix[nx][ny]
                    else:
                        continue
                result = max(temp,result)

print(result)
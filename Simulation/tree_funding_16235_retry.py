import sys
sys.stdin = open("tree_funding_16235.txt")

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

# 봄: 자신의 나이 만큼 양분을 먹고 나이가 1증가, 여러개의 나무가 있다면 어린 나무부터 양분 섭취
from _collections import deque

def iswall(x,y):
    if x < 0 or y < 0:
        return False
    elif x >= len(matrix) or y >= len(matrix):
        return False
    else:
        return True

def spring():
    for i in range(N):
        for j in range(N):
            length = len(matrix[i][j])
            if length == 0:
                continue
            else:
                stack = []
                for l in range(length):
                    temp = matrix[i][j].pop()
                    if energy[i][j] < temp:
                        dead_tree[i][j] = matrix[i][j]
                        dead_tree[i][j].append(temp)
                        break
                    else:
                        energy[i][j] -= temp
                        stack.append(temp+1)
                matrix[i][j] = stack[::-1]
# 여름: 봄에 죽은 나무가 양분으로 변함. 죽은 나무//2 만큼 양분 증가
def summer():
    for i in range(N):
        for j in range(N):
            length = len(dead_tree[i][j])
            for l in range(length):
                temp = dead_tree[i][j].pop()
                energy[i][j] += (temp)//2

# 가을: 나무가 번식. 번식하는 나무는 나이가 5의 배수이며 인접한 8개의 칸에 나이가 1인 나무가 생김
def fall():
    for i in range(N):
        for j in range(N):
            for l in matrix[i][j]:
                if l % 5 == 0:
                    for k in range(8):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if iswall(nx,ny):
                            matrix[nx][ny].append(1)
# 겨울: 땅에 양분을 추가, matrix만큼

def winter():
    for i in range(N):
        for j in range(N):
            energy[i][j] += data[i][j]

def search():
    result = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j]:
                result += len(matrix[i][j])
    return result
global N
N, M, K = map(int,input().split())
# 겨울에 심길 나무 갯수
data = [list(map(int,input().split())) for _ in range(N)]
# matrix: 상도가 심은 나무 상태 나이
matrix = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x,y,z = map(int,input().split())
    matrix[x-1][y-1].append(z)
# 양분 상태
energy = [[5 for _ in range(N)] for _ in range(N)]
# 죽은 나무들
dead_tree = [[[] for _ in range(N)] for _ in range(N)]
dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

for _ in range(K):
    spring()
    summer()
    fall()
    winter()
print(search())
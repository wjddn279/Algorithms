# N <100000 이므로 N^2 하면 메모리 터져서 인접행렬 불가

import sys
sys.stdin = open("line.txt")
# N , M : 학생들 번호는 1~N, M개줄에 키를 비교한 두 학생 A,B
# A가 B학생의 앞에 서야함
def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

from _collections import deque
N,M = map(int,input().split())
matrix = [[] for _ in range(N+1)]
ind = [0 for _ in range(N+1)]
result = []
# matrix[i][j] = 1 -> i 는 j보다 앞에 선다
for i in range(M):
    x,y = map(int,input().split())
    if y not in matrix[x]:
        matrix[x].append(y)
        ind[y] += 1

queue = deque()
for i in range(1,N+1):
    if ind[i] == 0:
        queue.append(i)
        result.append(i)
while queue:
    x = queue.popleft()
    for i in matrix[x]:
        ind[i] -= 1
        if ind[i] == 0:
            queue.append(i)
            result.append(i)
print(*result)
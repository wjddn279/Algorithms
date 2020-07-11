# N <= 100 이므로 N^2 을 해도 큰 수가 아니다 그러므로 인접 행렬 형태로 만드는 것도 상관없다

import sys
sys.stdin = open("toy.txt")

from _collections import deque

def prin(a):
    for i in range(len(a)):
        print(*a[i])
    print()

# 부품 -> 기본 부품, 중간 부품
# 기본 부품 -> 조립 될 수 없는 부품, 중간 부품 -> 합쳐져서 만들어짐
# 1 ~ N-1 : 기본 부품이나 중간 부품의 번호
# N : 완제품의 번호
# X,Y,Z : X를 만드는데 부품 y가 k개 필요하다

N = int(input())
M = int(input())
# atom[x][y] : 부품 x를 만들기 위해 부품 y가 k 개 필요하다
# state[x] : 부품 x를 만들기 위해 필요한 부품 갯수
atom = [[0 for _ in range(N+1)] for _ in range(N+1)]
state = [0 for _ in range(N+1)]
queue = deque()
funda = []
for _ in range(M):
    x,y,z = map(int,input().split())
    atom[x][y] = z
    state[x] += 1

for i in range(1,N+1):
    if state[i] == 0:
        atom[i][i] = 1
        queue.append(i)
        funda.append(i)

# prin(atom)
# 기본 갯수
funda_num = len(funda)
while queue:
    x = queue.popleft()
    for i in range(1,N+1):
        if atom[i][x] != 0 and i != x:
            state[i] -= 1
            if state[i] == 0 and i != N:
                queue.append(i)
    if x not in funda:
        temp = [0 for _ in range(N + 1)]
        for i in range(1,N+1):
            if atom[x][i] != 0:
                for j in range(1,N+1):
                    temp[j] = temp[j] + atom[x][i] * atom[i][j]
        atom[x] = temp

temp = [0 for _ in range(N + 1)]
for i in range(1,N+1):
    if atom[N][i] != 0:
        for j in range(1,N+1):
            temp[j] = temp[j] + atom[N][i] * atom[i][j]
atom[N] = temp

for i in funda:
    print('{} {}'.format(i,atom[N][i]))

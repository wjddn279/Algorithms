import sys
sys.stdin = open("input.txt")

import heapq
# 컵라면 갯수
N = int(input())
data = [[] for _ in range(N+1)]
for i in range(N):
    a,b = map(int,input().split())
    data[a].append(b)
for i in range(N):
    if len(data[i]):
        data[i].sort(reverse=True)

heap = []
heapq.heapify(heap)
for i in range(1,N+1):
    if len(data[i]) != 0:
        # 제일 큰 거 추가하고
        heapq.heappush(heap,data[i][0])
        # 그다음꺼 부터 도는데, 지금 있는 것 중에 가장 작은 거 보다 다음께
        for j in range(1,len(data[i])):
            temp = heapq.heappop(heap)
            # 크다? 그럼 다시 넣고 끝
            if temp > data[i][j]:
                heapq.heappush(heap,temp)
                break
            # 아니다? 그럼 데이터를 넣고 다시
            else:
                heapq.heappush(heap,data[i][j])
    else:
        heapq.heappush(heap,0)
print(sum(heap))
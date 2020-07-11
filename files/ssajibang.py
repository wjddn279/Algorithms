import sys
sys.stdin = open("ssajibang.txt")


# N : 사람의 수  P: 컴퓨터 이용 시작 시간 Q: 컴퓨터 종료 시간

from heapq import *

N = int(input())
times = [list(map(int,input().split())) for _ in range(N)]
frequency = []
computers,temp = [], []
heapify(computers)
heapify(temp)
times.sort(reverse=True)
# temp 에는 시간이 작은 것만 담긴다.
# 근데 처음것이 크다 -> 들어갈 자리가 없다
# 새로운 컴퓨터 만듬
while times:
    time = times.pop()
    length = len(frequency)
    # temp 에 담겨있는 것은 당연히 time[0] 보다 큰 것들이므로 돌려줄 필요 없다.
    for _ in range(len(computers)):
        value,number = heappop(computers)
        if value < time[0]:
            heappush(computers,(value,number))
            break
        else:
            heappush(temp, (number, value))

    if len(temp) == 0:
        heappush(computers,(time[1],length+1))
        frequency.append(1)
    elif len(temp) != 0:
        number,value = heappop(temp)
        heappush(computers,(time[1],number))
        frequency[number-1] += 1
print(frequency)
print(len(computers))
print(*frequency)
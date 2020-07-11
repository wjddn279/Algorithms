import sys
sys.stdin = open("ssajibang.txt")

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
    length = len(computers)
    for _ in range(len(computers)):
        number,value = heappop(computers)
        if value < time[0]:
            heappush(computers,(number,time[1]))
            frequency[number-1] += 1
            break
        else:
            heappush(temp, (number, value))
    if len(temp) == length:
        heappush(computers,(length+1,time[1]))
        frequency.append(1)

    computers = computers + temp
    temp = []
print(len(computers))
print(*frequency)
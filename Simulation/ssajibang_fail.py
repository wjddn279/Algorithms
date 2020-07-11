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
    length = len(frequency)
    if len(computers) == 0:
        heappush(computers,(time[1],length+1))
        frequency.append(1)
    else:
        for _ in range(len(computers)):
            value,number = heappop(computers)
            if value > time[0]:
                heappush(computers,(value,number))
                break
            else:
                heappush(temp, (number, value))
        if len(temp) == 0:
            heappush(computers,(time[1],length+1))
            frequency.append(1)
        else:
            number,value = heappop(temp)
            heappush(computers,(time[1],number))
            frequency[number-1] += 1
print(len(computers))
print(*frequency)
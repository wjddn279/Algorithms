import sys
sys.stdin = open("input.txt")

import heapq
from _collections import deque

N = int(input())

upper, lower = [], []
medium = [0,0]
temp1 = int(input())
print(temp1)
temp2 = int(input())
print(min(temp1,temp2))
if temp1 > temp2:
    medium[0],medium[1] = temp2,temp1
else:
    medium[0], medium[1] = temp1, temp2
medium = deque(medium)
right, left = 0, 0
for i in range(N-2):
    temp = int(input())
    if temp < medium[0]:
        heapq.heappush(lower,-temp)
        left += 1
    elif temp > medium[1]:
        heapq.heappush(upper,temp)
        right += 1
    else:
        a = medium[0]
        medium[0] = temp
        heapq.heappush(lower,-a)
        left += 1
    if (i+3)%2 == 1:
        if left > right : print(medium[0])
        else: print(medium[1])
    else:
        if right < left:
            a = - heapq.heappop(lower)
            medium.appendleft(a)
            heapq.heappush(upper,medium.pop())
            left -= 1
            right += 1
        elif right > left:
            a = heapq.heappop(upper)
            heapq.heappush(lower,-medium.popleft())
            medium.append(a)
            right -= 1
            left += 1
        print(min(medium))


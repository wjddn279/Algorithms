import sys
sys.stdin = open("input.txt")

from _collections import deque

def iswall(x,y):
    if not 0 <= x <= 200000: return False
    if not 0 <= y <= 200000: return False
    else: return True

def solve(start_cony,brown,time):

    queue =deque()
    queue.append((start_cony,brown,time))
    visited = {}
    while queue:
        cony,brown,time = queue.popleft()
        if cony == brown:
            return time-1
        next_cony = start_cony+(time*(time+1)//2)
        if iswall(next_cony,brown-1) and (next_cony,brown-1) not in visited:
            queue.append((next_cony,brown-1,time+1))
            visited[(next_cony,brown-1)] = 0
        if iswall(next_cony,brown+1) and (next_cony,brown+1) not in visited:
            queue.append((next_cony,brown+1,time+1))
            visited[(next_cony, brown + 1)] = 0
        if iswall(next_cony,brown*2) and (next_cony,brown*2) not in visited:
            queue.append((next_cony,2*brown,time+1))
            visited[(next_cony, 2*brown)] = 0
    return -1

print(solve(23124,22425,1))
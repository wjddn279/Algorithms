from _collections import deque

def solution(food_times, k):
    queue, total = [], len(food_times)
    for idx,food in enumerate(food_times):
        queue.append([food,idx])
    queue.sort()
    print(queue)

print(solution([3,1,2],5))
from _collections import deque
import random
def solution(ball, order):
    answer,wait = [], {}
    ball = deque(ball)
    for num in order:

        if ball:
            if ball[-1] == num:
                answer.append(ball.pop())
            elif ball[0] == num:
                answer.append(ball.popleft())
            else:
                wait[num] = 0

        while ball and (ball[0] in wait or ball[-1] in wait):
            if ball[-1] in wait:
                answer.append(ball.pop())
            elif ball[0] in wait:
                answer.append(ball.popleft())
    return answer

a = list(range(1,1000000))
b = list(range(1,1000000))
random.shuffle(a)
random.shuffle(b)

print(solution(a,b))
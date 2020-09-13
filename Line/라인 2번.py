from _collections import deque

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

print(solution([1, 2, 3, 4, 5, 6],[6, 2, 5, 1, 4, 3]))
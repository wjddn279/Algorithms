from math import ceil,floor
def solution(w,h):
    answer = w * h
    now, temp = 0, 0
    for x in range(1,w+1):
        y = h/w * x
        temp += (ceil(y)-now)
        now = floor(y)
        if y - floor(y) == 0:
            break
    temp = temp * (w//x)
    answer -= temp
    return answer

print(ceil(1/100000000000))
print(solution(8,12))
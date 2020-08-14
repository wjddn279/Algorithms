# 22:20

import sys
sys.stdin = open("input.txt")


from itertools import permutations

ining = int(input())
data = [list(map(int,input().split())) for _ in range(ining)]

# 타순 0~8
member = [1,2,3,4,5,6,7,8]
candidate = permutations(member,8)
value = 0
for hit_list in candidate:
    num, result, cnt = 0, 0, 0
    ini,b1,b2,b3,out = 0,0,0,0,0
    while ini < ining :
        # 1 2 3 0 4 5 6 7 9
        if num%9 == 3:
            now = data[ini][0]
        elif num%9 > 3:
            now = data[ini][hit_list[num%9-1]]
        else:
            now = data[ini][hit_list[num%9]]
        # 0이면 아웃, 아웃되면 아웃카운트 하나 추가
        if now == 0:
            out += 1
        # 1루타하면 한칸씩 이동
        elif now == 1:
            result += b3
            b3 = b2
            b2 = b1
            b1 = 1
        elif now == 2:
            result = result + b3 + b2
            b3 = b1
            b2 = 1
            b1 = 0
        elif now == 3:
            result += b3 + b2 + b1
            b3 = 1
            b2 = 0
            b1 = 0
        else:
            result = result + b3 + b2 + b1 + 1
            b3 = 0
            b2 = 0
            b1 = 0
        num += 1
        # 아웃 카운트 3개 -> step 초기화 및 이닝 ++
        if out == 3:
            b1,b2,b3 = 0,0,0
            out = 0
            ini += 1
    value = max(result,value)
print(value)
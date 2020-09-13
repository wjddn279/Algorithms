from itertools import combinations

def solution(orders, course):
    answer = []
    comb = [{} for _ in range(11)]
    for order in orders:
        for num in course:
            for temp in combinations(order,num):
                temp = tuple(sorted(list(temp)))
                if temp not in comb[num]:
                    comb[num][temp] = 1
                else:
                    comb[num][temp] += 1
    for dic in comb:
        max_val = 0
        for num in dic.values():
            if num > max_val:
                max_val = num
        if max_val < 2:
            continue
        for key,value in dic.items():
            if value == max_val:
                answer.append(''.join(key))
    return sorted(answer)

print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))
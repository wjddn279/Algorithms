import sys
sys.stdin = open("../input.txt")

def prin(a):
    for i in a:
        print(i)
    print()

def powerset(n,k,step):
    if n == k:
        branch.append(step)
        return
    for i in range(3):
        powerset(n,k+1,step+[i])

con2num, num2con = {}, {}
for idx,country in enumerate(input().split()):
    con2num[country] = idx
    num2con[idx] = country
matrix = [[0 for _ in range(4)] for _ in range(4)]
branch = []
powerset(6,0,[])
for _ in range(6):
    A,B,win,draw,lose = input().split()
    matrix[con2num[A]][con2num[B]] = float(win)
    matrix[con2num[B]][con2num[A]] = float(lose)
match = [(0,1),(3,2),(3,0),(1,2),(0,2),(1,3)]

total = [0 for _ in range(4)]
cnt = 0
for flow in branch:
    ranking = [0 for i in range(4)]
    prob = 1
    for idx, result in enumerate(flow):
        # 0 : A 승리, 1: 무승부, 2: B 승리
        A, B = match[idx]
        if result == 0 and matrix[A][B] != 0:
            ranking[A] += 3
            prob *= matrix[A][B]
        elif result == 2 and matrix[B][A] != 0:
            ranking[B] += 3
            prob *= matrix[B][A]
        elif result == 1 and (matrix[A][B] + matrix[B][A]) != 1:
            ranking[A] += 1
            ranking[B] += 1
            prob *= (1-matrix[A][B] - matrix[B][A])
        else:
            break
    else:
        cnt += 1
        max_val,se_val = max(ranking),-1
        first,second = [], []
        for num in ranking:
            if num != max_val and num > se_val:
                se_val = num
        print(ranking)
        for i,num in enumerate(ranking):
            if num == max_val:
                first.append(i)
            elif num == se_val:
                second.append(i)
        print(first,second)
        if len(first) == 1:
            total[first[0]] += 1
            if len(second) == 1:
                total[second[0]] += 1
            if len(second) > 1:
                for i in second:
                    total[i] += 1/len(second)
        elif len(first) == 2:
            total[first[0]] += 1
            total[first[1]] += 1
        elif len(first) > 2:
            for i in first:
                total[i] += 2 / len(first)

for num in total:
    print(num/cnt)
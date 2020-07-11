import sys
sys.stdin = open("input4.txt")

T =  int(input())

def search(point1,point2):
    parent1,parent2 = [point1], [point2]
    for j in range(0,len(data),2):
        for i in range(0,len(data),2):
            if data[len(data)-1-i] in parent1 and data[len(data)-i-2] not in parent1:
                parent1.append(data[len(data)-i-2])
            if data[len(data)-1-i] in parent2 and data[len(data)-i-2] not in parent2:
                parent2.append(data[len(data)-i-2])
    print(parent1)
    print(parent2)
    for i in parent1:
        for j in parent2:
            if i == j:
                return i

def sub_tree(a):
    sub = [a]
    for i in range(0,len(data),2):
        if data[i] in sub and data[i+1] not in sub:
            sub.append(data[i+1])
    return len(sub)
for test_case in range(1,T+1):
    node,line,point1,point2 = map(int,input().split())
    data = list(map(int,input().split()))
    a = search(point1,point2)
    b = sub_tree(a)
    print('#{} {} {}'.format(test_case,a,b))
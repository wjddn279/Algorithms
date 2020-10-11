import sys
sys.stdin = open("input.txt")

# 1시 35분
from _collections import deque

T = int(input())

def deci(N):
    result = 0
    for idx,val in enumerate(N[::-1]):
        result += mapping[val] * pow(16,idx)
    return result

for test_case in range(1,T+1):
    N, K = map(int,input().split())
    da = deque(list(input()))
    data = []
    for _ in range(N):
        data += da
    dic = {}
    mapping = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    length = N//4
    for s in range(N):
        for i in range(4):
            dic[''.join(data[s+length*i:s+length*(i+1)])] = 0
    decimal = [deci(num) for num in dic.keys()]
    decimal.sort(reverse=True)
    print('#{} {}'.format(test_case,decimal[K-1]))
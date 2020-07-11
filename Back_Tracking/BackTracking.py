import sys
sys.stdin = open("input7.txt")

T = int(input())

def Permutation(n,k,sum):
    global min_sum
    if n == k:
        if min_sum > sum:
            min_sum = sum
    elif min_sum < sum:
        return
    else:
        for i in range(k,n):
            a[i],a[k] = a[k],a[i]
            Permutation(n,k+1,sum+data[k][a[k]])
            a[i],a[k] = a[k],a[i]

for test_case in range(1,T+1):
    can = []
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    a = list(range(N))
    min_sum = 9999999
    Permutation(N,0,0)
    print(min_sum)
